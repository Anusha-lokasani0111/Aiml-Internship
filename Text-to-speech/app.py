import streamlit as st
from gtts import gTTS
from validator import validate_text
from tts_engine import generate_speech


# ---------- Page Config ----------
st.set_page_config(page_title="Text to Speech", layout="centered")

st.markdown("""
<style>

/* Background Same Old Colour */
.stApp {
    background: linear-gradient(135deg, #f5f7fa, #c3cfe2);
    font-family: 'Segoe UI', sans-serif;
}

/* Main Card */
.main-card {
    background-color: white;
    padding: 30px;
    border-radius: 12px;
    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
    max-width: 750px;
    margin: auto;
    position: relative;
}

/* ----- Top Empty Box with Heading ----- */
.main-card::before {
    content: "Text to Speech Converter";
    display: block;
    background: #eef2f7;
    padding: 18px;
    border-radius: 12px;
    text-align: center;
    font-size: 28px;
    font-weight: 700;
    color: #2c3e50;
    margin-bottom: 20px;
}

/* Hide Original Heading (duplicate kakunda) */
.title-text {
    display: none;
}

/* Subtitle */
.subtitle-text {
    text-align: center;
    font-size: 16px;
    color: #7f8c8d;
    margin-bottom: 25px;
}

/* Button */
.stButton > button {
    background-color: #4CAF50;
    color: white;
    font-size: 16px;
    padding: 10px 25px;
    border-radius: 8px;
    border: none;
}

.stButton > button:hover {
    background-color: #43a047;
}

</style>
""", unsafe_allow_html=True)

# ---------- UI ----------
st.markdown('<div class="main-card">', unsafe_allow_html=True)

st.markdown('<div class="title-text">Text to Speech Converter</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle-text">Convert text into natural sounding speech</div>', unsafe_allow_html=True)

text = st.text_area("Enter text to convert to speech")
voice_type = st.selectbox(
    "Select Voice Type",
    ["Male", "Female"]
)

accent = st.selectbox(
    "Select Accent",
    ["US English", "Indian English", "British English"]
)
# Map accent to gTTS language code
if accent == "US English":
    voice_lang = "en"
elif accent == "Indian English":
    voice_lang = "en-in"
elif accent == "British English":
    voice_lang = "en-gb"


voice_lang = st.selectbox(
    "Select Voice / Language",
    ["en", "en-in"]
)

speed = st.slider("Speech Speed", 0.5, 1.5, 1.0)
volume = st.slider("Volume", 0.5, 1.5, 1.0)

if st.button("Generate Speech"):
    try:
        clean_text = validate_text(text)
    except ValueError as e:
        st.error(str(e))
        st.stop()
    else:
        audio_file = generate_speech(clean_text, voice_type)


        st.success("Speech generated successfully")
        st.audio(audio_file)

st.markdown('</div>', unsafe_allow_html=True)
