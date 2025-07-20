import streamlit as st
import requests
import base64
import os

# Page Config
st.set_page_config(page_title="🤖 DomainBot", layout="centered")

# Load & Display Icon
image_path = "bot.png"
if os.path.exists(image_path):
    with open(image_path, "rb") as img_file:
        b64_image = base64.b64encode(img_file.read()).decode()
    st.markdown(f"""
        <div style='text-align: center;'>
            <img src="data:image/png;base64,{b64_image}" alt="Chatbot Icon" width="160"/>
        </div>
    """, unsafe_allow_html=True)

# Title
# st.markdown("<h1 style='text-align: center;'>DomainBot</h1>", unsafe_allow_html=True)

# CSS Styling
st.markdown("""
<style>
.chat-box {
    background-color: #f8f9fa;
    border-radius: 12px;
    padding: 15px;
    margin-top: 20px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
}
.user-msg {
    background-color: #e3f2fd;
    padding: 12px;
    border-radius: 10px;
    color: #0d47a1;
    font-weight: bold;
    margin-bottom: 10px;
}
.bot-msg {
    background-color: #e8f5e9;
    padding: 12px;
    border-radius: 10px;
    color: #2e7d32;
    font-weight: 500;
}
textarea {
    font-size: 16px !important;
}
</style>
""", unsafe_allow_html=True)

# --- Sidebar or Top Controls ---
# st.markdown("### 🔧 Configuration", unsafe_allow_html=True)

MODEL_NAME = st.selectbox("🔁 Select LLM Model", ["gemma3:4b", "tinyllama:latest", "phi3:3.8b"])
DOMAIN = st.selectbox("🌐 Select Knowledge Domain", ["Space", "IT", "Medical"])

TEMPERATURE = st.slider(
    "🎛️ Creativity / Temperature",
    min_value=0.0,
    max_value=2.0,
    step=0.1,
    value=0.7,
    help="Controls randomness: Low = focused, High = creative"
)

# System Prompts
DOMAIN_PROMPTS = {
    "Space": "You are an AI astrophysicist. Only answer questions related to space, astronomy, or astrophysics. If irrelevant, say 'I only answer space-related questions.'",
    "IT": "You are an IT expert. Only answer technical questions about programming, networking, and software systems. Say 'This question is out of my IT scope' if irrelevant.",
    "Medical": "You are a medical advisor. Only answer medical or health-related queries. Otherwise say: 'I can only assist with medical questions.'"
}

# Build Final Prompt
def build_prompt(user_query):
    return f"{DOMAIN_PROMPTS[DOMAIN]}\n\nUser: {user_query}\n\nAI:"

# Send to Ollama
def ask_model(prompt):
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "temperature": TEMPERATURE,
        "stream": False
    }
    try:
        res = requests.post("http://localhost:11434/api/generate", json=payload)
        return res.json().get("response", "[No response]") if res.status_code == 200 else f"[Error {res.status_code}]"
    except Exception as e:
        return f"[Error] {e}"

# User Input
with st.form("chat_form"):
    user_input = st.text_area("💬 Ask your question", height=150)
    submitted = st.form_submit_button("Submit")

# Display
if submitted and user_input.strip():
    with st.spinner("Consulting the domain expert..."):
        final_prompt = build_prompt(user_input)
        answer = ask_model(final_prompt)

    st.markdown(f"""
    <div class='chat-box'>
        <div class='user-msg'>👤 <strong>You:</strong><br>{user_input}</div>
        <div class='bot-msg'>🤖 <strong>DomainBot:</strong><br>{answer}</div>
    </div>
    """, unsafe_allow_html=True)
