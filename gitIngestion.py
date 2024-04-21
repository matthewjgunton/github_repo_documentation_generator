import anthropic
import os
import shutil
import subprocess

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
def dfs_directory_files(start_path):
    if not os.path.isdir(start_path):
        raise ValueError(f"The provided path {start_path} is not a directory or does not exist.")
    
    stack = [start_path]
    all_files = []

    while stack:
        current_path = stack.pop()
        print(current_path)
        for entry in sorted(os.listdir(current_path), reverse=True):  # Reverse sort to maintain usual DFS order
            full_path = os.path.join(current_path, entry)
            if os.path.isdir(full_path):
                stack.append(full_path)
            elif os.path.isfile(full_path):
                all_files.append(full_path)

    return all_files

### callLLM
def callLLM(translate, doctor, summarize):
    # get relevant documents >> for now that's only the most recent one
    doctor['Date'] = pd.to_datetime(doctor['Date'], format='mixed')
    sorted_df = doctor.sort_values(by='Date', ascending=False)
    values = sorted_df.iloc[0]
    msg = []
    prompt = f'<document>{values["Data"]}</document> Read the document.'

    # Spanish Translation
    if translate:
        prompt += " Then translate the document into Spanish."

    if summarize:
        prompt += " Then summarize the document."

    msg.append(
        {"role": "user", "content": prompt}
    )
    
    message = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=1024,
        messages=msg
    )

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


import subprocess

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
    url = "https://github.com/matthewjgunton/doctormalpractice.git"
    if download_repo(url, target_dir=dir):
        files = dfs_directory_files(dir)
    else:
        print("ERROR RUNNING SCRIPT")




