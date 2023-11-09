import os
import streamlit as st
from langchain.llms import OpenAI
from dotenv import load_dotenv

load_dotenv()

def get_openai_response(query):
    llm = OpenAI(model_name="text-davinci-003",temperature=0.5, openai_api_key = os.getenv("OPENAI_API_KEY"))
    response = llm(query)
    return response

st.set_page_config(page_title="LangChain ChatBot", page_icon=":earth_americas:", layout="wide")

st.header("LangChain ChatBot")

input = st.text_input("Enter your query here",key="input")

response = get_openai_response(input)

submit = st.button("Submit")

if submit:
    st.write(response)
