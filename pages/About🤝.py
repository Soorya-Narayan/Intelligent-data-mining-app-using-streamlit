import streamlit as st

# Center-aligning the title using HTML
st.set_page_config(page_title="About", page_icon="🤝")
st.markdown("<h1 style='text-align: center;'>Docompanion Team 🤝</h1>", unsafe_allow_html=True)
st.write("")

# Highlighted box with provided details
st.markdown(
    """
    **Input Handling:**

    - Supports image, text, document, YouTube URL, and web URL inputs.
    - Utilizes libraries like PIL, PyPDF2, and Requests for processing.

    **Chatbot:**

    - Powered by OpenAI's GPT model for quick responses.
    - Enhances user interaction and provides assistance.

    **User Interface (UI):**

    - Developed using Streamlit for a user-friendly experience.
    - Optional visual enhancements with Streamlit-lottie.

    **API Integration:**

    - Integrates Google API for language-related tasks.
    - Utilizes environment variables managed by python-dotenv.

    **Backend Processing:**

    - Employs libraries like Transformers for NLP tasks.
    - Executes image processing, text analysis, and API calls.

    **AI Models:**

    - Utilizes Google's Generative AI models for creative tasks.
    - Leverages LangChain for language-related functionalities.

    **Deployment:**

    - Deployable on platforms like Heroku, AWS, or Google Cloud.

    **Workflow:**

    **User Interaction:**

    - Users access the app through a browser.
    - Choose input type and interact with the chatbot.

    **Input Processing:**

    - Processes input based on user choice.

    **Backend Processing:**

    - Executes backend tasks using appropriate libraries and APIs.

    **Response Generation:**

    - Generates responses based on processed input and user queries.

    **Displaying Results:**

    - Presents results via the web interface.

    **Feedback and Iteration:**

    - Allows user feedback for improvements.
    """
)
