from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()

os.environ['LANGCHAIN_TRACING_V2']="true"
os.environ['LANGCHAIN_API_KEY']=os.getenv("LANGCHAIN_API_KEY")

# prompt part

prompt=ChatPromptTemplate.from_messages(
    [
    ("system","You are a helpful assistant so please respond to the users question."),
    ('user','Question:{question}')

]
)
ollama = Ollama(model="llama3")
output_parase=StrOutputParser()
chain=prompt|ollama|output_parase

##streamlit page part
st.title('LangChain Assistant')
input_text=st.text_input("what do you want to ask?")

if input_text: 
    st.write(chain.invoke({'question':input_text}))
