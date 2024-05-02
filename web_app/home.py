import streamlit as st
from io import BytesIO
from utils import groq_helper, set_shared_variable, parse_problems, init_state, extract_text_from_pdf, get_shared_variable, question
import re
from llama_index.readers.github import GithubRepositoryReader, GithubClient
from llama_index.core import VectorStoreIndex
import os
from dotenv import load_dotenv
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import Settings
from llama_index.core import (
    SimpleDirectoryReader,
    VectorStoreIndex,
    StorageContext,
)
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Document
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core import StorageContext
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
import chromadb
from llama_index.llms.groq import Groq
from git_ingestion import GitIngestion
import time

load_dotenv()
os.environ['TOKENIZERS_PARALLELISM'] = 'true'
github_token = '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'

@st.cache_resource
def setup_data_store(url):

    #dir = "./git_src"
    #git_ingestion = GitIngestion(url, "claude", dir)
    #text = git_ingestion.run()

    documents = SimpleDirectoryReader("../chrome_extension").load_data()

    #Embed Documents
    Settings.embed_model = HuggingFaceEmbedding(
        model_name="BAAI/bge-small-en-v1.5"
    )

    start_time = time.time()

    client = chromadb.PersistentClient(path="./cache")
    chroma_collection = client.get_or_create_collection(name="my_collection")
    
    vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
    storage_context_ingestion = StorageContext.from_defaults(vector_store=vector_store)
    index_ingestion = VectorStoreIndex.from_documents(
        documents, storage_context=storage_context_ingestion, embed_model=Settings.embed_model
        )


    end_time = time.time()
    time_taken = end_time - start_time
    print(f"Total Embedding Time taken: {time_taken:.6f} seconds")


    # Create the query engine
    llm = Groq(model="mixtral-8x7b-32768", api_key=os.environ["GROQ_API_KEY"])
    query_engine_ingestion = index_ingestion.as_query_engine(llm=llm)
    return query_engine_ingestion

#Simple app to extract the math problems from an uploaded PDF file of a math textbook
def app():
    init_state()
    query_engine_ingestion = setup_data_store('https://github.com/matthewjgunton/CSE341project.git')

    #Streamlit portion:
    st.title("Repo Tools App")

    # Link to textbook used in testing
    link_to_data = "https://github.com/Significant-Gravitas/AutoGPT.git"
    st.markdown(f'<label for="file_uploader">Note: This app is a WIP. It is not guaranteed to work with large files or other repos, and so far has only been tested on the following repo: <a href="{link_to_data}" target="_blank">Link</a></label>', unsafe_allow_html=True)
    
    st.title("Chat with Lesson Planner Assistant:")

    st.session_state.msg_counter = 0

    if "messages" not in st.session_state:
            st.session_state.messages = []
            st.session_state.messages.append({
                "role": "assistant",
                "content": f"""I am an intelligent AI assistant that can help you understand your Git Repos! Leveraging the power of RAG, I am aware of the contents of your uploaded repository.
                
                """
            })

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # React to user input
    if prompt := st.chat_input("What do you want to ask the LLM?"):
        # Display user message in chat message container
        st.chat_message("user").markdown(prompt)
        # Add user message to chat history
        
        
        st.session_state.messages.append({"role": "user", 
                                            "content": prompt,
                                            'user_message_no': st.session_state.msg_counter})
        
        raq_query = prompt
        rag_response_ingestion = query_engine_ingestion.query(raq_query)

        prompt_for_model_ingestion = f'''
        
        
        You are a helpful assistant that helps developers understand their Git repos. Here are the files in their repo
    
        {rag_response_ingestion}
        
        Below the teacher will input their query to you:        
        ''' + prompt
        
        print(st.session_state.messages) 
        response_ingestion = groq_helper(prompt=prompt_for_model_ingestion)
        llm_response_ingestion = response_ingestion.choices[0].message.content

        with st.chat_message("assistant"):
            st.markdown(llm_response_ingestion)
            st.markdown("# Ingestion Response:")
            # Add LLM response to chat history
            st.session_state.messages.append({"role": "assistant", 
                                            "content": llm_response_ingestion,
                                            "assistant_msg_counter": st.session_state.msg_counter})
            st.session_state.msg_counter += 1
        
if __name__ == "__main__":
    app()
