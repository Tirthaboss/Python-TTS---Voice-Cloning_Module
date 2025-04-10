from tts_voice_cloning import TTSVoiceCloning

def main():
    tts = TTSVoiceCloning()
    audio_file = "path_to_audio_file.wav"  # Replace with actual file path
    text = "Hello, this is a test of the voice cloning system."
    output_audio = tts.generate_cloned_speech(text, audio_file)
    print(f"Output audio saved to: {output_audio}")

if __name__ == "__main__":
    main()
