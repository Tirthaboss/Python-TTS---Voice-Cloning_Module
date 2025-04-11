import streamlit as st
import os
from tts_voice_cloning import TTSVoiceCloning

# Initialize module
tts_module = TTSVoiceCloning()

# Sidebar
st.sidebar.title("TTS Toolkit")
menu = st.sidebar.radio("Select Tool", ["Text to Speech", "Speech to Text", "Voice Clone"])

st.title("Advanced TTS Module with Voice Cloning")

if menu == "Text to Speech":
    st.subheader("Text to Speech")
    text = st.text_area("Enter text to synthesize", "")
    if st.button("Generate Speech"):
        output = tts_module.synthesize_speech(text)
        st.success("Speech generated!")
        st.audio(output)

elif menu == "Speech to Text":
    st.subheader("Speech to Text")
    audio_file = st.file_uploader("Upload audio (WAV only)", type=["wav"])
    if audio_file and st.button("Transcribe"):
        st.info("This feature is under development.")

elif menu == "Voice Clone":
    st.subheader("Voice Cloning")
    text = st.text_area("Enter text to speak in cloned voice", "")
    audio_file = st.file_uploader("Upload voice sample (MP3/WAV)", type=["mp3", "wav"])
    if st.button("Generate Cloned Voice") and text and audio_file:
        # Save uploaded file temporarily
        temp_path = f"temp_{audio_file.name}"
        with open(temp_path, "wb") as f:
            f.write(audio_file.read())

        output_audio = tts_module.generate_cloned_speech(text, temp_path)
        st.success("Cloned voice generated!")
        st.audio(output_audio)

        os.remove(temp_path)

