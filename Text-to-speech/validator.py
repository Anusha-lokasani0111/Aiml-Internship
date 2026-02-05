import re

def validate_text(text: str) -> str:
    if not text or text.strip() == "":
        raise ValueError("Text input cannot be empty")

    # Remove unsupported special characters
    cleaned_text = re.sub(r"[^a-zA-Z0-9.,!? ]+", "", text)

    return cleaned_text.strip()























































# ---------- Custom CSS ----------
# st.markdown("""
# <style>
# .stApp {
#     background: linear-gradient(135deg, #f5f7fa, #c3cfe2);
#     font-family: 'Segoe UI', sans-serif;
# }

# .main-card {
#     background-color: white;
#     padding: 30px;
#     border-radius: 12px;
#     box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
#     max-width: 750px;
#     margin: auto;
# }

# .title-text {
#     text-align: center;
#     font-size: 36px;
#     font-weight: 700;
#     color: #2c3e50;
# }

# .subtitle-text {
#     text-align: center;
#     font-size: 16px;
#     color: #7f8c8d;
#     margin-bottom: 25px;
# }

# .stButton > button {
#     background-color: #4CAF50;
#     color: white;
#     font-size: 16px;
#     padding: 10px 25px;
#     border-radius: 8px;
#     border: none;
# }

# .stButton > button:hover {
#     background-color: #43a047;
# }
# </style>
# """, unsafe_allow_html=True)
