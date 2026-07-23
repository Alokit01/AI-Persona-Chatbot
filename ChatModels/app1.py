import os
import streamlit as st
from dotenv import load_dotenv

from langchain.chat_models import init_chat_model
from langchain_core.messages import (
    SystemMessage,
    HumanMessage,
    AIMessage,
)

# ---------------- Load Environment ----------------
load_dotenv()

# Read API key from Streamlit Secrets when deployed
if "MISTRAL_API_KEY" in st.secrets:
    os.environ["MISTRAL_API_KEY"] = st.secrets["MISTRAL_API_KEY"]

# ---------------- Initialize Model ----------------
@st.cache_resource
def get_model():
    return init_chat_model("mistral-medium-3-5")

model = get_model()

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="AI Persona Chatbot",
    page_icon="🤖",
    layout="centered"
)

# ---------------- Persona Theme Configurations ----------------
MODES_CONFIG = {
    "🤬 Angry Mode": {
        "title": "Angry AI Assistant",
        "system_prompt": "You are an angry AI agent. Respond aggressively, impatiently, and short-tempered.",
        "bg_color": "#FFF5F5",
        "primary_accent": "#E53935",
        "header_gradient": "linear-gradient(135deg, #D32F2F, #9A0007)",
        "emojis": ["🤬", "😡", "💢", "🔥", "😤", "💥"]
    },
    "😂 Funny Mode": {
        "title": "Funny AI Assistant",
        "system_prompt": "You are a very funny AI agent. Respond with sharp humor, puns, and witty jokes.",
        "bg_color": "#FFFBEB",
        "primary_accent": "#D97706",
        "header_gradient": "linear-gradient(135deg, #F59E0B, #B45309)",
        "emojis": ["😂", "🤣", "🤪", "🤡", "😜", "🎉"]
    },
    "🌧️ Sad Mode": {
        "title": "Sad AI Assistant",
        "system_prompt": "You are a sad AI agent. Respond in a melancholic, gloomy, and emotionally heavy tone.",
        "bg_color": "#F0F4FF",
        "primary_accent": "#3B82F6",
        "header_gradient": "linear-gradient(135deg, #2563EB, #1E40AF)",
        "emojis": ["🌧️", "😢", "💧", "☁️", "💔", "🥀"]
    },
    "📚 Teacher Mode": {
        "title": "Philosophical Teacher AI",
        "system_prompt": "You are a teacher AI agent. Respond in a deep, highly structured, and philosophical manner.",
        "bg_color": "#F0FDF4",
        "primary_accent": "#059669",
        "header_gradient": "linear-gradient(135deg, #10B981, #047857)",
        "emojis": ["📚", "🎓", "💡", "🏛️", "📖", "✨"]
    },
    "💻 Coder Mode": {
        "title": "Coder AI Assistant",
        "system_prompt": "You are a specialized coding AI agent. Answer ONLY coding, programming, and software questions. Refuse all non-technical general chit-chat.",
        "bg_color": "#F0FDFA",
        "primary_accent": "#0D9488",
        "header_gradient": "linear-gradient(135deg, #14B8A6, #0F766E)",
        "emojis": ["💻", "⚡", "⌨️", "🚀", "🐛", "👾"]
    }
}

# ---------------- Floating Background Emojis & Custom CSS ----------------
def apply_custom_ui(bg_color, primary_accent, emojis):
    emoji_html = "".join([f'<span class="floating-emoji">{e}</span>' for e in emojis * 2])
    
    custom_css = f"""
    <style>
    /* Main App Background */
    .stApp {{
        background-color: {bg_color} !important;
        color: #0F172A !important;
    }}
    
    /* Background Floating Emojis */
    .emoji-bg-container {{
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        overflow: hidden;
        z-index: 0;
        pointer-events: none;
    }}

    .floating-emoji {{
        position: absolute;
        display: block;
        font-size: 2.2rem;
        opacity: 0.12;
        animation: floatUp 15s linear infinite;
        bottom: -100px;
    }}

    .floating-emoji:nth-child(1)  {{ left: 5%;  animation-delay: 0s;  animation-duration: 12s; }}
    .floating-emoji:nth-child(2)  {{ left: 20%; animation-delay: 3s;  animation-duration: 16s; }}
    .floating-emoji:nth-child(3)  {{ left: 35%; animation-delay: 1s;  animation-duration: 11s; }}
    .floating-emoji:nth-child(4)  {{ left: 50%; animation-delay: 5s;  animation-duration: 14s; }}
    .floating-emoji:nth-child(5)  {{ left: 65%; animation-delay: 2s;  animation-duration: 13s; }}
    .floating-emoji:nth-child(6)  {{ left: 80%; animation-delay: 4s;  animation-duration: 15s; }}
    .floating-emoji:nth-child(7)  {{ left: 12%; animation-delay: 7s;  animation-duration: 13s; }}
    .floating-emoji:nth-child(8)  {{ left: 42%; animation-delay: 8s;  animation-duration: 17s; }}
    .floating-emoji:nth-child(9)  {{ left: 73%; animation-delay: 6s;  animation-duration: 12s; }}
    .floating-emoji:nth-child(10) {{ left: 88%; animation-delay: 9s;  animation-duration: 15s; }}

    @keyframes floatUp {{
        0% {{ transform: translateY(0) rotate(0deg); opacity: 0; }}
        20% {{ opacity: 0.15; }}
        80% {{ opacity: 0.15; }}
        100% {{ transform: translateY(-115vh) rotate(360deg); opacity: 0; }}
    }}

    /* Layering Protection */
    .stChatFloatingInputContainer, .main .block-container {{
        position: relative;
        z-index: 1;
    }}

    /* Typography */
    .stMarkdown, p, span, label {{
        color: #0F172A !important;
        font-weight: 500;
    }}

    /* --- FIXED CHAT INPUT BOX: DARK BG + BRIGHT WHITE TEXT --- */
    /* Outer Box Wrapper */
    div[data-testid="stChatInput"] {{
        background-color: #1E293B !important;
        border-radius: 14px !important;
        border: 2px solid {primary_accent} !important;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1) !important;
    }}

    /* Inner Text Area Box */
    div[data-testid="stChatInput"] textarea,
    div[data-baseweb="textarea"],
    div[data-baseweb="textarea"] textarea {{
        background-color: #1E293B !important;
        color: #FFFFFF !important;
        -webkit-text-fill-color: #FFFFFF !important; /* Forces typed text to stay white */
        font-size: 1rem !important;
        font-weight: 600 !important;
    }}

    /* Placeholder Styling */
    div[data-testid="stChatInput"] textarea::placeholder {{
        color: #94A3B8 !important;
        -webkit-text-fill-color: #94A3B8 !important;
    }}

    /* Buttons */
    .stButton > button {{
        background-color: #FFFFFF !important;
        color: #0F172A !important;
        border: 2px solid #E2E8F0 !important;
        font-weight: 600 !important;
        border-radius: 10px !important;
        transition: all 0.2s ease;
    }}
    .stButton > button:hover {{
        border-color: {primary_accent} !important;
        color: {primary_accent} !important;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    }}
    </style>

    <div class="emoji-bg-container">
        {emoji_html}
    </div>
    """
    st.markdown(custom_css, unsafe_allow_html=True)


# ---------------- Session State Controls ----------------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "mode_selected" not in st.session_state:
    st.session_state.mode_selected = False

if "active_mode" not in st.session_state:
    st.session_state.active_mode = None

def reset_chat():
    st.session_state.messages = []
    st.session_state.mode_selected = False
    st.session_state.active_mode = None
    st.rerun()


# ==========================================================
# HOME PAGE
# ==========================================================
if not st.session_state.mode_selected:

    apply_custom_ui(
        bg_color="#F8FAFC",
        primary_accent="#4F46E5",
        emojis=["🤖", "✨", "💬", "🎭", "⚡"]
    )

    st.markdown(
        """
        <div style='text-align: center; padding: 20px 0 10px 0;'>
            <h1 style='color: #0F172A; font-weight: 800; font-size: 2.2rem;'>🤖 AI Persona Studio</h1>
            <p style='color: #475569; font-size: 1.05rem;'>Select a personality mode to transform your chat experience</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    selected_mode_key = st.radio(
        "**Select Personality Mode:**",
        list(MODES_CONFIG.keys()),
        index=0
    )

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("🚀 Start Chatting", use_container_width=True):
        config = MODES_CONFIG[selected_mode_key]

        st.session_state.messages = [
            SystemMessage(content=config["system_prompt"])
        ]
        st.session_state.mode_selected = True
        st.session_state.active_mode = selected_mode_key
        st.rerun()


# ==========================================================
# CHAT PAGE
# ==========================================================
else:
    mode_info = MODES_CONFIG[st.session_state.active_mode]

    apply_custom_ui(
        bg_color=mode_info["bg_color"],
        primary_accent=mode_info["primary_accent"],
        emojis=mode_info["emojis"]
    )

    # Header
    st.markdown(
        f"""
        <div style="
            background: {mode_info['header_gradient']};
            padding: 20px;
            border-radius: 14px;
            text-align: center;
            color: #FFFFFF !important;
            margin-bottom: 20px;
            box-shadow: 0 4px 14px rgba(0,0,0,0.12);
        ">
            <h2 style="margin: 0; font-weight: 700; color: #FFFFFF !important;">{mode_info['title']}</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Control Buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🏠 Change Mode", use_container_width=True):
            reset_chat()

    with col2:
        if st.button("🗑️ Clear Chat", use_container_width=True):
            sys_msg = st.session_state.messages[0]
            st.session_state.messages = [sys_msg]
            st.rerun()

    st.markdown("---")

    # Chat Messages History
    for msg in st.session_state.messages[1:]:
        if isinstance(msg, HumanMessage):
            with st.chat_message("user"):
                st.write(msg.content)
        elif isinstance(msg, AIMessage):
            with st.chat_message("assistant"):
                st.write(msg.content)

    # User Chat Input
    prompt = st.chat_input("Type your message... (Type '0' to return home)")

    if prompt:
        if prompt.strip() == "0":
            reset_chat()

        st.session_state.messages.append(HumanMessage(content=prompt))
        with st.chat_message("user"):
            st.write(prompt)

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = model.invoke(st.session_state.messages)
                st.write(response.content)

        st.session_state.messages.append(AIMessage(content=response.content))
        st.rerun()