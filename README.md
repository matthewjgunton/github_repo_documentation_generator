# Overview

# chrome extension
- has the files that will quickly summarize your PR request when you are on the github pr page

# web_app
- Simple Python App built using [Streamlit](https://docs.streamlit.io/) & [LlamaIndex](https://docs.llamaindex.ai/en/stable/) to implement Retrieval Augmented Generation (RAG) on your Git Repos.

## Web App Configuration

- First run: `$ cd web_app`
- Install libraries:
    - Using **pip** and pyenv:
        - Create new virtual environment:
            - `python -m venv venv`
        - Activate environment:
            - `source venv/bin/activate`
        - Install libraries:
            - `pip install -r requirements.txt`
    - Using **conda**:
        - Create new conda env:
            - `conda create --name env`
        - Activate environment:
            - `conda activate env`
        - Install libraries
            - `conda install --yes --file requirements.txt` 

## Web App Usage

Now that you have installed the libraries, to run your app, cd into the /web_app directory and run the following command:

`streamlit run home.py`


### GitHub Personal Access Token
Before running the script, you will need to pass in a github token on line 27 of [home.py](/web_app/home.py).

See the official GitHub Documentation for instructions on how to generate a Personal Access Token: [link](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens).



### Binary and Unparsable Files
Note that embedding time will vary depending on the size of the git repo you are embedding. The program cannot parse binary files. If you encounter errors, be sure to indicate the extensions of binary files on line 33 of [home.py](/web_app/home.py) by passing in the `ignored_extensions` and `ignored_directories` dictionaries like so:


```
git_ingestion = GitIngestion(
    url, 
    "claude", 
    dir,
    ignored_extensions = set([".jar", ".class",".ico", ".png", ".jpeg", ".jpg", ".pdf"]),     
    ignored_directories = set([".git", ".github", "frontend", "imgs", "arena", "oracle"])
```



