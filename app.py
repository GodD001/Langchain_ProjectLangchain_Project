from langchain.llms import OpenAI
from dotenv import load_dotenv

load_dotenv()
import os
import streamlit as st
import openai



os.environ["OPEN_AI_KEY"]="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"

def get_openai_respone(question):
    llm = OpenAI(openai_api_key=os.environ["OPEN_AI_KEY"], model_name="text-davinci-003",temperature=0.5)
    response=llm(question)
    return response

st.set_page_config(page_title="Q&A Demo")


st.header('Langchain Application')


input =st.text_input("Input:", key="input")
response = get_openai_respone(input)

submit =st.button("Ask the question")

if submit:
    st.subheader("The Response is")
    st.write(response)