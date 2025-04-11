import streamlit as st
import os
from voicecloning import TTSVoiceCloning

# Initialize TTS module
tts_module = TTSVoiceCloning()

# Sidebar
st.sidebar.title("TTS Toolkit")
menu = st.sidebar.radio("Select Tool", ["Text to Speech", "Speech to Text", "Voice Clone"])

# Main title
st.title("Advanced TTS Module with Voice Cloning")

# TEXT TO SPEECH
if menu == "Text to Speech":
    st.subheader("Text to Speech")
    text = st.text_area("Enter text to synthesize", "")
    if st.button("Generate Speech"):
        if text.strip():
            output = tts_module.synthesize_speech(text)
            st.success("Speech generated!")
            st.audio(output)
        else:
            st.warning("Please enter some text.")

# SPEECH TO TEXT (Not implemented yet)
elif menu == "Speech to Text":
    st.subheader("Speech to Text")
    audio_file = st.file_uploader("Upload audio (WAV only)", type=["wav"])
    if audio_file and st.button("Transcribe"):
        st.info("This feature is under development.")

# VOICE CLONING
elif menu == "Voice Clone":
    st.subheader("Voice Cloning")
    text = st.text_area("Enter text to speak in cloned voice", "")
    audio_file = st.file_uploader("Upload voice sample (MP3/WAV)", type=["mp3", "wav"])
    
    if st.button("Generate Cloned Voice"):
        if not text.strip():
            st.warning("Please enter text.")
        elif not audio_file:
            st.warning("Please upload an audio file.")
        else:
            # Save uploaded file temporarily
            temp_path = f"temp_{audio_file.name}"
            with open(temp_path, "wb") as f:
                f.write(audio_file.read())

            # Generate speech
            output_audio = tts_module.generate_cloned_speech(text, temp_path)
            st.success("Cloned voice generated!")
            st.audio(output_audio)

            # Clean up
            os.remove(temp_path)
