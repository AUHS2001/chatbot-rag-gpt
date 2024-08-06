import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage
from dotenv import load_dotenv
from openai import OpenAI
from pinecone import ServerlessSpec, Pinecone as PC
from langchain_pinecone import Pinecone
from langchain_openai import OpenAIEmbeddings

from utils import *


load_dotenv()

openai_client = OpenAI()

pc = PC()
spec = ServerlessSpec(cloud="aws", region="") #write the region here
index_name = "" #write the index name here
index = pc.Index(index_name)
embeddings = OpenAIEmbeddings()
vectorstore = Pinecone(index, embeddings, "text")

# app config
st.set_page_config(page_title="ML Chatbot", page_icon="🤖")
st.title("Chatbot")


# session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        AIMessage(content="Hello, I am a ML Chatbot. How can I help you?"),
    ]


# conversation
for message in st.session_state.chat_history:
    if isinstance(message, AIMessage):
        with st.chat_message("AI"):
            st.write(message.content)
    elif isinstance(message, HumanMessage):
        with st.chat_message("Human"):
            st.write(message.content)

# user input
user_query = st.chat_input("Type your message here...")
if user_query is not None and user_query != "":
    st.session_state.chat_history.append(HumanMessage(content=user_query))

    with st.chat_message("Human"):
        st.markdown(user_query)

    with st.spinner("thinking..."):
        with st.chat_message("AI"):
            similar_docs = get_similiar_docs(vectorstore, user_query)
            contexts = [item.page_content for item in similar_docs]
            augmented_query = "\n---\n".join(contexts) + "\n-----\n" + user_query
            response = generate_response(openai_client, prompt, augmented_query)

            st.write(response)

    st.session_state.chat_history.append(AIMessage(content=response))
