from anthropic import Anthropic
from groq import Groq
from dotenv import load_dotenv
import os
import shutil
import subprocess
import traceback
import time
import chardet
from file_info import FileInfo
import requests

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
def dfs_directory_files(start_path, ignored_directories={".git"}, ignored_extensions={'.tmp', '.log', '.jar', '.env', '.Driver', '.DS_Store'}, ignored_files={"README.md"}):
    print(f"START PATH: {start_path}")
    if not os.path.isdir(start_path):
        raise ValueError(f"The provided path {start_path} is not a directory or does not exist.")

    root = FileInfo(None, start_path, None)
    stack: list["FileInfo"] = [root]

    with open("source.txt", "w", encoding="utf-8") as output_file:
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

            for entry in sorted(entries, reverse=True):
                # Reverse sort to maintain usual DFS order
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
                        output_file.write(f"<------------{full_path}----------->\n\n")
                        try:
                            with open(full_path, "rb") as file:
                                result = chardet.detect(file.read())
                                encoding = result['encoding']
                            with open(full_path, "r", encoding=encoding) as file:
                                output_file.write(file.read())
                        except (UnicodeDecodeError, LookupError):
                            output_file.write(f"[Unable to decode {full_path}]\n")
                        output_file.write(f"\n<------------{full_path}----------->\n\n")

    with open("source.txt", "r", encoding="utf-8") as output_file:
        source_text = output_file.read()
    
    return source_text

            
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
def summarize_file(file_text, file_path, client):
    prompt = f'<document><name>{file_path}</name><text>{file_text}</text></document>'
    return callLLM(prompt, False, client)

def callAnthropic(prompt:str, isDir:bool, client):
    sysPrompt = ""
    if isDir:
        sysPrompt = "Read above documents. Give a succinct summary that explains all of them. Give your response in markdown"
    else:
        sysPrompt = "Read the source code and write a succinct and accurate summary. Give your response in markdown"

    msg = []
    msg.append(
        {"role": "user", "content": prompt + " " +sysPrompt}
    )

    message = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=1024,
        messages=msg
    )
    return message.content[0].text

def callGroq(prompt:str, isDir:bool, client):

    sysPrompt = ""
    if isDir:
        sysPrompt = "[Inst]Read the user's source code. It will be enclosed within the <document> tag with the filename enclosed within the <name> tag. There may be multiple documents. Write a succinct and accurate summary of all documents. Give your response in markdown[/Inst]"
    else:
        sysPrompt = "[Inst]Read the user's source code. It will be enclosed within the <document> tag with the filename enclosed within the <name> tag. Write a succinct and accurate summary. Give your response in markdown[/Inst]"

    msg = [
        {"role": "system", "content": sysPrompt}
    ]
    msg.append(
        {"role": "user", "content": prompt}
    )

    chat_completion = client.chat.completions.create(
        messages=msg,
        model="mixtral-8x7b-32768",
        max_tokens=1024,
        stream=False
    )

    return chat_completion.choices[0].message.content

### possible error here in bigger files
def summarizeDir(list_of_summaries, list_of_file_names, batch_size, client):
    results_list = []
    index_file_name = 0
    while len(list_of_summaries) > 0:
        time.sleep(2)
        msg = []   
        current_batch = 0
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
        list_of_summaries = list_of_summaries[index_of_list_of_summaries:]
        results_list.append(callLLM(prompt, True, client))
    return results_list

# wrapper to let us quickly switch between providers
def callLLM(prompt, isDir, client):

    if isinstance(client, Groq):
        return callGroq(prompt, isDir, client)
    if isinstance(client, Anthropic):
        return callAnthropic(prompt, isDir, client)

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
                text += "##" + key + ":\n" + value + "\n"
            text += "\n\n"
            print({f"KEY, VALUE: {key}, {value}"})
        # Open the file in write mode. This will overwrite the existing content.
        with open(file_path, 'w', encoding='utf-8') as md_file:
            md_file.write(text)
            print(f"Text has been successfully written to {file_path}")
            print(f"TEXT VARIABLE: {text}")
            print(file_path)
        return text
    except Exception as e:
        # If any errors occur during file opening or writing, raise an exception
        raise Exception(f"Failed to write to the file: {e}")

def summarization(node: "FileInfo", map_filepath_to_sum: dict, client):
    summary = None
    print("Summarization: " + node.file_path)
    if len(node.children) == 0:
        summary = retry_wrapper(callLLM, get_file_text(node.file_path), node.file_path, client)
    else:
        summary_list = []
        for child in node.children:
            summary_list.append(summarization(child, map_filepath_to_sum, client))
        summary = retry_wrapper( summarizeDir, summary_list, [child.file_path for child in node.children], 10000, client)
    map_filepath_to_sum[node.file_path] = summary
    return summary




class GitIngestion:
    def __init__(self, url: str, provider:str, dir:str = "./git_src",
                 
                 ignored_extensions:set = ([".jar", ".class", ".ico", ".png", ".jpeg", ".jpg", ".pdf"]), 
                 ignored_directories:set=([".git", ".github", "frontend", "imgs", "arena", "oracle"])
                 ):
 
        self.url = url
        self.ignored_extensions=ignored_extensions
        self.ignored_directories=ignored_directories
        load_dotenv()
        if provider == "groq":
            self.client = Groq(api_key=os.environ["GROQ_API_KEY"])
        if provider == "claude":
            self.client = Anthropic(
                api_key=os.environ["ANTHROPIC_API_KEY"]
            )
        self.dir = dir

    def run(self):
        try:
            clean_up_dir(self.dir)
            if download_repo(self.url, target_dir=self.dir):
                source = dfs_directory_files(self.dir, ignored_directories=self.ignored_directories, ignored_extensions=self.ignored_extensions)
                return source
            else:
                print("ERROR RUNNING SCRIPT")
        except Exception:
            print(traceback.format_exc())
            clean_up_dir(self.dir)

    def cleanup(self):
        clean_up_dir(self.dir)


def get_commit_diff(repo_owner, repo_name, commit_sha):
    """
    Retrieves the diff for a given commit in a GitHub repository.

    Args:
        repo_owner (str): The owner of the GitHub repository.
        repo_name (str): The name of the GitHub repository.
        commit_sha (str): The SHA-1 hash of the commit.

    Returns:
        str: The diff for the specified commit.
    """
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/git/commits/{commit_sha}"
    headers = {
        "Accept": "application/vnd.github.v3.diff"
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raise an exception for non-2xx status codes

    return response.text

if __name__ == "__main__":
    url = "https://github.com/matthewjgunton/CSE341project.git"
    instance = GitIngestion(url, "claude")
    source = instance.run()
    print(source)


