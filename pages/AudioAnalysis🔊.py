import streamlit as st
from google.cloud import speech_v1p1beta1 as speech
import librosa
import io
import os

# Function to convert audio bytes to array
def convert_bytes_to_array(audio_bytes):
    audio_bytes = io.BytesIO(audio_bytes)
    audio, sample_rate = librosa.load(audio_bytes)
    return audio, sample_rate

# Function to transcribe audio using Google Speech-to-Text
def transcribe_audio(audio_bytes):
    client = speech.SpeechClient()

    # Convert audio bytes to array
    audio_array, sample_rate = convert_bytes_to_array(audio_bytes)

    # Prepare the audio for Google Speech-to-Text
    audio = speech.RecognitionAudio(content=audio_bytes.getvalue())
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=sample_rate,
        language_code="en-US",
    )

    # Transcribe audio
    response = client.recognize(config=config, audio=audio)

    # Extract the transcription
    transcription = ""
    for result in response.results:
        transcription += result.alternatives[0].transcript

    return transcription

def main():
    st.set_page_config(page_title="AudioAnalysis", page_icon="🔊")
    st.title("Audio Analysis 🔊")

    # File uploader for audio files
    uploaded_audio = st.file_uploader("Upload audio file", type=["mp3", "wav", "ogg"])

    if uploaded_audio:
        st.audio(uploaded_audio, format='audio/wav')

        # Button to transcribe audio
        if st.button("Transcribe"):
            transcribed_text = transcribe_audio(uploaded_audio)
            st.write("Transcribed Text:")
            st.write(transcribed_text)

if __name__ == "__main__":
    # Set the environment variable for Google Application Credentials
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path/to/your/service-account-file.json"
    main()
