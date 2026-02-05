import pyttsx3

def generate_speech(text, voice_type):
    engine = pyttsx3.init()

    voices = engine.getProperty('voices')

    # Select voice based on gender
    if voice_type == "Male":
        engine.setProperty('voice', voices[0].id)
    else:
        if len(voices) > 1:
            engine.setProperty('voice', voices[1].id)

    engine.save_to_file(text, "output.mp3")
    engine.runAndWait()

    return "output.mp3"
