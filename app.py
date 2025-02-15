import os
import streamlit as st
import google.generativeai as ai

api_key=os.getenv("GOOGLE_API_KEY")
ai.configure(api_key=api_key)

system_prompt=(
                "You are an AI assistant using google ai API. Your task is to analyze the python code provided by the user."
                "First , Identify any bugs , identation errors, any errors or mistake in python code. Then , Provide a 'Bug report' section listing the issues and a 'Corrected code' section with corrected code ."
                "However , If the code is correct without any error or bugs or identation error, simply respond 'Do not generate bug report in this case because code is correct without any error or bugs.'"
                "In any case if a user enter code in other language like c++, java etc... except python,politely decline and tell them to ask only python code for review"
                )
model=ai.GenerativeModel(model_name="models/gemini-2.0-pro-exp-02-05", system_instruction=system_prompt)
st.title("Python Code Reviewer using AI")
user_prompt=st.text_area(label="Enter your Python code here...",height=200)
butn=st.button("CLICK ME")
if butn==True:
    response=model.generate_content(user_prompt)
    st.write(response.text)