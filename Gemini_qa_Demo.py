from dotenv import load_dotenv
load_dotenv() 

import streamlit as st
import os
import google.generativeai as genai

##Both way you can load the API KEY
GOOGLE_API_KEY="asdfghj!@#$%^&*"
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## function to load Gemini Pro model and get repsonses from it
model=genai.GenerativeModel("gemini-pro") 
chat = model.start_chat(history=[])

def get_gemini_response(question):
    response=chat.send_message(question,stream=True)
    return response

##initialize our streamlit application

st.set_page_config(page_title="Question_Answer Demo")

st.header("Google Gemini")

# Initialize session state for chat history if it doesn't exist
if 'chat_history_conv' not in st.session_state:
    st.session_state['chat_history_conv'] = []

input=st.text_input("Input: ",key="input", placeholder="Enter your Prompt here...")
submit=st.button("Click me....")

if submit and input:
    response=get_gemini_response(input)
    # Add user query and response to session state chat history
    st.session_state['chat_history_conv'].append(("USER :::", input))
    st.subheader("The Response is")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history_conv'].append(("BOT :::", chunk.text))
st.subheader("The Conversation History is")
    
for role, text in st.session_state['chat_history_conv']:
    st.write(f"{role}: {text}")
    



    

