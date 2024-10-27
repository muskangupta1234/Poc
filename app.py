import streamlit as st
from google.cloud import speech, texttospeech
import openai
from moviepy.editor import VideoFileClip, AudioFileClip
from pydub import AudioSegment
#import io
import requests

# Set up the Azure OpenAI API key and endpoint
api_key = "22ec84421ec24230a3638d1b51e3a7dc"  # Replace with your actual API key
endpoint = "https://internshala.openai.azure.com/openai/deployments/gpt-4o/chat/completions?api-version=2024-08-01-preview"

# Define the headers for the request
headers = {
    "Content-Type": "application/json",
    "api-key": api_key
}

st.title("Azure OpenAI Chatbot")
st.write("This app connects to Azure's OpenAI Service for text generation.")

# User input
user_input = st.text_input("You:", "Hello, how are you today?")
if user_input:
    # Create the request payload
    data = {
        "messages": [
            {"role": "User", "content": "You are a helpful AI assistant."},
            {"role": "user", "content": user_input}
        ],
        "max_tokens": 100
    }
    
# Make the request to Azure OpenAI
    response = requests.post(endpoint, headers=headers, json=data)
    
# Process and display the response
    if response.status_code == 200:
        response_data = response.json()
        reply = response_data["choices"][0]["message"]["content"]
        st.write(f"AI: {reply}")
        
    else:
        st.write(f"Request failed with status code {response.status_code}: {response.text}")     
     
    
                   
