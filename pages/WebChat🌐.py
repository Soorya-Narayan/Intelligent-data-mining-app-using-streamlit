import os
import streamlit as st
from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage
from PIL import Image
import google.generativeai as genai
from langchain.document_loaders import WebBaseLoader

# Load environment variables from .env file
load_dotenv()

# Configure the Google API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Define the prompt template
prompt_template = """You are a web blog summarizer. You will be taking the content of a web page 
and summarizing the entire content and providing the important summary in points within 250 words. 
Please provide the summary of the text given here: """

def extract_web_content(url):
    try:
        loader = WebBaseLoader(url)
        data = loader.load()
        content = ""
        for doc in data:
            content += " " + doc.page_content
        return content
    except Exception as e:
        raise e

# Function to get response from Gemini API
def get_gemini_response(input_text, image=None):
    model = genai.GenerativeModel('gemini-pro')
    if input_text and image:
        response = model.generate_content([input_text, image])
    elif input_text:
        response = model.generate_content(input_text)
    else:
        response = model.generate_content(image)
    return response.text

def main():
    # Set the title and subtitle of the app
    st.set_page_config(page_title="WebChat", page_icon="🌐")
    st.title('WebChat🌐')
    
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = [
            AIMessage(content="Hello, How can I help you?"),
        ]

    url = st.text_input("", placeholder="Insert website URL here")

    # Process the URL as soon as entered
    if url:
        content_text = extract_web_content(url)
        if content_text:
            summary = get_gemini_response(prompt_template + content_text)
            st.markdown("## Detailed Notes:")
            st.write(summary)
            st.session_state.chat_history.append(AIMessage(content=summary))

    # Display chat history
    for message in st.session_state.chat_history:
        if isinstance(message, AIMessage):
            with st.chat_message("AI"):
                st.write(message.content)
        elif isinstance(message, HumanMessage):
            with st.chat_message("Human"):
                st.write(message.content)

    # User input
    user_query = st.chat_input("Type your message here...")
    
    image = None

    

    if user_query is not None and user_query != "":
        st.session_state.chat_history.append(HumanMessage(content=user_query))

        with st.chat_message("Human"):
            st.markdown(user_query)

        with st.chat_message("AI"):
            response_text = get_gemini_response(user_query, image)
            st.write(response_text)

        st.session_state.chat_history.append(AIMessage(content=response_text))

if __name__ == '__main__':
    main()
