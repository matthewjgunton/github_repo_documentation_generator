from llama_index.readers.github import GithubRepositoryReader, GithubClient
from llama_index.core import VectorStoreIndex
import os
from dotenv import load_dotenv
import faiss
from llama_index.vector_stores.faiss import FaissVectorStore
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import Settings
from llama_index.core import (
    SimpleDirectoryReader,
    load_index_from_storage,
    VectorStoreIndex,
    StorageContext,
)
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


#set equal to dimensions of selected embedding model
d = 384

faiss_index = faiss.IndexFlatL2(d)

vector_store = FaissVectorStore(faiss_index=faiss_index)
storage_context = StorageContext.from_defaults(vector_store=vector_store)
index = VectorStoreIndex.from_documents(
    documents, storage_context=storage_context
)

# save index to disk
index.storage_context.persist()

# load index from disk
vector_store = FaissVectorStore.from_persist_dir("./storage")
storage_context = StorageContext.from_defaults(
    vector_store=vector_store, persist_dir="./storage"
)
index = load_index_from_storage(storage_context=storage_context)

# set Logging to DEBUG for more detailed outputs

llm = Groq(model="mixtral-8x7b-32768", api_key=os.environ["GROQ_API_KEY"])

query_engine = index.as_query_engine(llm=llm)

response = query_engine.query("What is the data contained in this input?")
print(response)
