import streamlit as st
import torch
from transformers import pipeline
import librosa
import io

# Function to convert audio bytes to array
def convert_bytes_to_array(audio_bytes):
    audio_bytes = io.BytesIO(audio_bytes)
    audio, sample_rate = librosa.load(audio_bytes)
    return audio

# Function to transcribe audio
def transcribe_audio(audio_bytes):
    device = "cuda:0" if torch.cuda.is_available() else "cpu"

    # Initialize the speech recognition pipeline
    pipe = pipeline(
        task="automatic-speech-recognition",
        model="openai/whisper-small",
        device=device,
    )

    # Convert audio bytes to array
    audio_array = convert_bytes_to_array(audio_bytes)
    
    # Transcribe audio
    prediction = pipe(audio_array)["text"]

    # Print the transcription in the terminal
    print("Transcription:", prediction)

    return prediction

def main():
    st.set_page_config(page_title="AudioAnalysis", page_icon="🔊")
    st.title("Audio Analysis 🔊")

    # File uploader for audio files
    uploaded_audio = st.file_uploader("Upload audio file", type=["mp3", "wav", "ogg"])

    if uploaded_audio:
        st.audio(uploaded_audio, format='audio/wav')

        # Button to transcribe audio
        if st.button("Transcribe"):
            transcribed_text = transcribe_audio(uploaded_audio.getvalue())
            st.write("Transcribed Text:")
            st.write(transcribed_text)

if __name__ == "__main__":
    main()
