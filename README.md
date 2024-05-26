
# Intelligent-data-mining-app-using-streamlit

A Guide for Building a Web App that Extracts and Retrieves Information from Audios, Images, Documents, and More.


## Introduction
Comprehensive guide on building an intelligent web application, which can extract and retrieve information from various media types such as texts, audios, images, URLs, and documents. This guide walks you through setting up your environment, installing necessary libraries, and creating interactive pages for different types of media analysis.


## Operational Guide

![Untitled (4)](https://github.com/Soorya-Narayan/Intelligent-data-mining-app-using-streamlit/assets/118114664/16d542c2-dd7c-416a-93f5-cc85ce774328)

1. Input Collection:

- Collect various data types (text, images, documents, audio, video) from sources like web URLs.
2. Data Chunking:

- Divide the collected data into smaller chunks.
3. Embedding Generation:

- Convert each chunk type into embeddings (numerical representations).
4. Embedding Storage:

- Store all embeddings in a vector database.
5. Question Embedding:

- Convert user questions into embeddings.
6. Similarity Search:

- Perform a similarity search in the vector database using the question embedding.
7. Answer Generation:

- Use a Language Model (LLM) to generate and rank answers from the relevant data embeddings, then present the results to the user.
## Setting up Python virtual environment
Creating virtual environment.
First, open a new folder in VSCode and add a new terminal. Run the following command to create a virtual environment:

```bash
python -m venv chat_venv
```
Activating the virtual environment.
Activate the virtual environment using:
```bash
chat_venv\Scripts\activate
```
## Installing necessary libraries.
Create a ```requirements.txt``` file and add the following libraries:

```txt
streamlit
streamlit-lottie
python-dotenv
google.generativeai
youtube_transcript_api
langchain
langchain_core
langchain_openai
PyPDF2
torch
transformers
librosa
chromadb
faiss-cpu
```

Use the following command to install all the dependencies at once.
(Make sure pip is installed.)
```bash
pip install -r requirements.txt
```
## Usage

Ensure that you have installed the required libraries and added the OpenAI API key & Google API key to the ```.env``` file.
```bash
streamlit run Home🏠.py
```


## 🔗 Links

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](www.linkedin.com/in/sooryanarayan)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://x.com/knowsoorya)
[![Medium](https://img.shields.io/badge/Medium-12100E?style=for-the-badge&logo=medium&logoColor=white)](https://medium.com/@sooryah)
[![Instagram](https://img.shields.io/badge/Instagram-%23E4405F.svg?style=for-the-badge&logo=Instagram&logoColor=white)](https://www.instagram.com/sooryeahhh/)

