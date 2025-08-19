import os
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
from langchain_ollama import OllamaLLM
import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are helpful assistant.Please respond to the question asked"),
        ("user","Question: {question}")
    ]
)

#streamlit framework

st.title("Langchain Demo with LLAMA2")
input_text=st.text_input("What question you have in mind ?")

#Ollama Lllama2 model
llm=OllamaLLM(model="llama3.2:1b")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))

