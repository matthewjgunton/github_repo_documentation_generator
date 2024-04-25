import os
from utils import groq_helper

from llama_index.core import SimpleDirectoryReader
from llama_index.core.node_parser import SentenceSplitter
#os.environ['OPENAI_API_KEY']=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
from llama_index.core import VectorStoreIndex
from llama_index.readers.github import GithubRepositoryReader
from IPython.display import Markdown, display
from dotenv import load_dotenv
import os

#import environment vars from .env to avoid sharing tokens
#the .env file is added to the gitignore so will need to manually create one and pass in your token
load_dotenv()


github_token = os.environ.get("GITHUB_TOKEN")
owner = "jerryjliu"
repo = "llama_index"
branch = "main"

documents = GithubRepositoryReader(
    github_token=github_token,
    owner=owner,
    repo=repo,
    use_parser=False,
    verbose=False,
    ignore_directories=["examples"],
).load_data(branch=branch)

index = VectorStoreIndex.from_documents(documents)

query_engine = index.as_query_engine()
response = query_engine.query(
    "What is the difference between VectorStoreIndex and SummaryIndex?",
    verbose=True,
)
    
#groq_helper(prompt = "Should I apply to a job at Meta?", modelid = 'llama3-70b-8192')

