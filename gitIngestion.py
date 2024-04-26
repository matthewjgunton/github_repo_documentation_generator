import anthropic
import os
import shutil
import subprocess
import traceback
import time

from file_info import FileInfo

client = anthropic.Anthropic(
    api_key="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"
)

### Download all the files
def download_repo(repo_url, target_dir=None):
    if target_dir is not None and not os.path.exists(target_dir):
        os.makedirs(target_dir)  # Create the directory if it does not exist
    elif target_dir is None:
        target_dir = '.'  # Set to current directory if no directory is provided

    cmd = ['git', 'clone', repo_url, target_dir]

    try:
        subprocess.run(cmd, check=True)
        print("Repository cloned successfully.")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Failed to clone repository: {e}")
        return False


### Run through each & make an API Call
#### Depth-First Search here
def dfs_directory_files(start_path, 
                        ignored_directories={".git"}, 
                        ignored_extensions={'.tmp', '.log'},
                        ignored_files={"README.md"}):
    if not os.path.isdir(start_path):
        raise ValueError(f"The provided path {start_path} is not a directory or does not exist.")
    
    root = FileInfo(None, start_path, None)
    stack : list["FileInfo"] = [root]
    while stack:
        parent = stack.pop()
        current_path = parent.file_path
        if root is None:
            root = parent
        try:
            entries = os.listdir(current_path)
        except PermissionError:
            # Skip directories where access is denied
            continue

        for entry in sorted(entries, reverse=True):  # Reverse sort to maintain usual DFS order
            full_path = os.path.join(current_path, entry)
            if os.path.isdir(full_path) and entry not in ignored_directories:
                child = FileInfo(None, full_path, parent)
                stack.append(child)
                parent.__add_children__(child)
            elif os.path.isfile(full_path) and entry not in ignored_files:
                # Check file extension against ignored_extensions set
                _, ext = os.path.splitext(entry)
                if ext not in ignored_extensions:
                    child = FileInfo(None, full_path, parent)
                    parent.__add_children__(child)
    return root                    

def retry_wrapper(fn, *args):
    max_tries = 3
    curr_try = 0
    while curr_try < max_tries:
        try:
            curr_try += 1
            print(" try " + str(curr_try))
            return fn(*args)
        except Exception:
            print(traceback.format_exc())
        print(curr_try)
        time.sleep(curr_try * 60)
    return None

### callLLM
def callLLM(file_text, file_path):
    msg = []
    prompt = f'<document><name>{file_path}</name><text>{file_text}</text></document> Read the source code and write a succinct and accurate summary. Give your response in markdown'
    msg.append(
        {"role": "user", "content": prompt}
    )

    message = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=1024,
        messages=msg
    )
    return message.content[0].text

### callLLM_summarize
### possible error here in bigger files
def summarizeDir(list_of_summaries, list_of_file_names, batch_size):
    results_list = []
    end_of_prompt = "Read above documents. Give a succinct summary that explains all of them. Give your response in markdown"
    index_file_name = 0
    while len(list_of_summaries) > 0:
        time.sleep(2)
        msg = []
        current_batch = len(end_of_prompt)
        index_of_list_of_summaries = 0
        prompt = ""
        for summary in list_of_summaries:
            file_name = list_of_file_names[index_file_name]
            prompt += f'<document><name>{file_name}</name><text>{summary}</text></document>'
            current_batch += len(prompt) 
            if current_batch >= batch_size:
                break
            index_of_list_of_summaries += 1
            index_file_name += 1
        prompt += end_of_prompt
        list_of_summaries = list_of_summaries[index_of_list_of_summaries:]
        msg.append(
            {"role": "user", "content": prompt}
        )
        message = client.messages.create(
            model="claude-3-haiku-20240307",
            max_tokens=1024,
            messages=msg
        )
        results_list.append(message.content[0].text)
    return results_list


def clean_up_dir(path):
    try:
        # Check if the directory exists
        if not os.path.exists(path):
            print("Directory does not exist.")
            return False

        # Recursively remove the directory and all its contents
        shutil.rmtree(path)
        print("Directory removed successfully.")
        return True
    except Exception as e:
        print(f"An error occurred while trying to remove the directory: {e}")
        return False

def get_file_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()
    
def write_to_file(map):
    try:
        file_path = "./output.md"
        text = ""
        
        for key, value in map.items():
            if isinstance(value, list):  # Check if the value is a list
                text += "## "+ key + ":\n"
                for item in value:
                    text += item +"\n"
            else:
                text += "## " + key + ":\n" + value + "\n"
            text += "\n\n"
            
        # Open the file in write mode. This will overwrite the existing content.
        with open(file_path, 'w', encoding='utf-8') as md_file:
            md_file.write(text)
            print(f"Text has been successfully written to {file_path}")
    except Exception as e:
        # If any errors occur during file opening or writing, raise an exception
        raise Exception(f"Failed to write to the file: {e}")

def summarization(node: "FileInfo", map_filepath_to_sum: dict):
    summary = None
    print("Summarization: " + node.file_path)
    if len(node.children) == 0:
        summary = retry_wrapper(callLLM, get_file_text(node.file_path), node.file_path)
    else:
        summary_list = []
        for child in node.children:
            summary_list.append(summarization(child, map_filepath_to_sum))
        summary = retry_wrapper( summarizeDir, summary_list, [child.file_path for child in node.children], 10000)
    map_filepath_to_sum[node.file_path] = summary
    return summary


def configure_git_credentials():
    """
    Configures git to use the credential helper for credential storage.
    will need more work later
    """
    try:
        # Set the credential helper to cache with a timeout (e.g., 1 hour = 3600 seconds)
        subprocess.run(['git', 'config', '--global', 'credential.helper', 'cache --timeout=3600'], check=True)
        print("Git configured to use credential helper with timeout.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to configure git: {e}")

if __name__ == "__main__":
    dir = "./git_src"
    url = "https://github.com/Significant-Gravitas/AutoGPT.git"
    try:
        if download_repo(url, target_dir=dir):
            root = dfs_directory_files(dir, 
                                        ignored_extensions={".jar", ".class", ".ico", ".png", ".jpeg", ".jpg"},
                                        ignored_directories={".git", ".github", "frontend", "imgs", "arena"})
            map_filepath_to_sum = {}
            summarization(root, map_filepath_to_sum)
            write_to_file(map_filepath_to_sum)
        else:
            print("ERROR RUNNING SCRIPT")
    except Exception:
        print(traceback.format_exc())
    finally:
        clean_up_dir(dir)




