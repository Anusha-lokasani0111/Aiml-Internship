import streamlit as st
from deepseek_api import ask_deepseek

# ================= Page Config =================
st.set_page_config(layout="wide")

# ================= Custom CSS =================
st.markdown("""
<style>

.main {
    display:flex;
    flex-direction:column;
    justify-content:center;
    align-items:center;
}

.title {
    text-align:center;
    margin-top:100px;
    font-size:38px;
    font-weight:600;
}

.subtitle {
    text-align:center;
    color:gray;
    margin-bottom:20px;
}

.chat-container {
    width:60%;
    margin:auto;
}

</style>
""", unsafe_allow_html=True)

# ================= Header =================
st.markdown('<div class="title">💬 DeepSeek Chat Assistant</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">A professional AI chat interface with error handling and logging</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Built for ML Internship Task • Streamlit + DeepSeek API</div>', unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# ================= Chat Memory =================
if "messages" not in st.session_state:
    st.session_state.messages = []

# ================= Chat Display =================
with st.container():

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

# ================= Bottom Input =================
prompt = st.chat_input("Type your message here...")

if prompt:

    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    reply = ask_deepseek(st.session_state.messages)

    st.session_state.messages.append({"role": "assistant", "content": reply})

    with st.chat_message("assistant"):
        st.markdown(reply)
