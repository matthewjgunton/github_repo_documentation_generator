from llama_index.readers.github import GithubRepositoryReader, GithubClient
from llama_index.core import VectorStoreIndex
import os
from dotenv import load_dotenv
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import Settings
from llama_index.core import (
    SimpleDirectoryReader,
    load_index_from_storage,
    VectorStoreIndex,
    StorageContext,
)
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core import StorageContext
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from IPython.display import Markdown, display
import chromadb

from llama_index.llms.groq import Groq

#load environment variables from dotenv
load_dotenv()
os.environ['TOKENIZERS_PARALLELISM'] = 'true'
github_token = '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'

#parse GitHub repo and load documents
owner="ng4567"
repo="LM2APA"
client = GithubClient(github_token=github_token)
reader = GithubRepositoryReader(owner=owner, repo=repo, github_client=client)
documents = reader.load_data(commit_sha='20af215c907c06910edd41e0de847979a8e29a91')

#Embed Documents
Settings.embed_model = HuggingFaceEmbedding(
    model_name="BAAI/bge-small-en-v1.5"
)


chroma_client = chromadb.EphemeralClient()
chroma_collection = chroma_client.create_collection("quickstart")

vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
storage_context = StorageContext.from_defaults(vector_store=vector_store)
index = VectorStoreIndex.from_documents(
    documents, storage_context=storage_context, embed_model=Settings.embed_model
)

llm = Groq(model="mixtral-8x7b-32768", api_key=os.environ["GROQ_API_KEY"])
query_engine = index.as_query_engine(llm=llm)


raq_query = "What did the author do growing up?"
print(f"Query: {raq_query}")

response = query_engine.query(raq_query)
print(response)


