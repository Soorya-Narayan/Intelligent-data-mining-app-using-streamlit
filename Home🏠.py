import json
import requests
import streamlit as st
from streamlit_lottie import st_lottie

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Function to load Lottie files
def load_lottie(url_or_path):
    if url_or_path.startswith("http"):
        return load_lottieurl(url_or_path)
    else:
        return load_lottiefile(url_or_path)

# Load Lottie animations
lottie_coding = load_lottie("lottiefiles/Home.json")

# Center-aligning the title using HTML
st.set_page_config(page_title="Home", page_icon="🏠")
st.markdown("<h1 style='text-align: center;'>Docompanion 🏠</h1>", unsafe_allow_html=True)
st.write("")

# Description of the app inside a box
with st.container():
    st.info("Introducing DoCompanion, the ultimate companion for information extraction and retrieval across various media types. With DoCompanion, you can seamlessly explore and interact with text, images, audio, documents, and even chatbot conversations—all in one powerful platform. \n DoCompanion is your go-to tool for extracting insights and retrieving valuable information from diverse sources. Whether you're analyzing text documents, browsing through image collections, listening to audio recordings, or reviewing important documents, DoCompanion empowers you to extract key insights with ease. \n ")
    # Add some vertical spacing
    st.write("")

# Center-align the Lottie animation
col1, col2, col3 = st.columns([1, 3, 1])  # Adjust the column ratios as needed
with col2:
    # Display Lottie animation
    st_lottie(
        lottie_coding,
        speed=1,
        reverse=False,
        loop=True,
        quality="low",
        height=400,  # Adjust the height as needed
        width=400,   # Adjust the width as needed
        key=None
    )
