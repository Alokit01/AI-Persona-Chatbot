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

# ---------------- Initialize Model ----------------

model = init_chat_model("mistral-medium-3-5")

# ---------------- Page Config ----------------

st.set_page_config(
    page_title="AI Personality Chatbot",
    page_icon="🤖",
    layout="centered"
)

# ---------------- Session State ----------------

if "messages" not in st.session_state:
    st.session_state.messages = []

if "mode_selected" not in st.session_state:
    st.session_state.mode_selected = False


# ---------------- Function to Reset ----------------

def go_home():
    st.session_state.messages = []
    st.session_state.mode_selected = False

    for key in ["title", "color1", "color2"]:
        if key in st.session_state:
            del st.session_state[key]

    st.rerun()


# ==========================================================
# HOME PAGE
# ==========================================================

if not st.session_state.mode_selected:

    st.markdown(
        """
        <h1 style='text-align:center;color:#4F46E5;'>
            🤖 AI Personality Chatbot
        </h1>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    st.subheader("Choose Your AI Personality")

    choice = st.radio(
        "",
        (
            "😂 Funny Mode",
            "😡 Angry Mode",
            "😢 Sad Mode"
        )
    )

    st.markdown("")

    if st.button("🚀 Start Chat", use_container_width=True):

        if choice == "😂 Funny Mode":

            system_prompt = (
                "You are a very funny AI assistant. "
                "Answer every question with humour and jokes."
            )

            title = "😂 Funny AI Chatbot"
            color1 = "#FFD54F"
            color2 = "#FF9800"

        elif choice == "😡 Angry Mode":

            system_prompt = (
                "You are an angry AI assistant. "
                "Reply aggressively and impatiently."
            )

            title = "😡 Angry AI Chatbot"
            color1 = "#EF5350"
            color2 = "#C62828"

        else:

            system_prompt = (
                "You are a sad AI assistant. "
                "Reply in a sad and emotional tone."
            )

            title = "😢 Sad AI Chatbot"
            color1 = "#42A5F5"
            color2 = "#1565C0"

        st.session_state.messages = [
            SystemMessage(content=system_prompt)
        ]

        st.session_state.mode_selected = True
        st.session_state.title = title
        st.session_state.color1 = color1
        st.session_state.color2 = color2

        st.rerun()


# ==========================================================
# CHAT PAGE
# ==========================================================

else:

    # Header

    st.markdown(
        f"""
        <div style="
            background:linear-gradient(90deg,{st.session_state.color1},{st.session_state.color2});
            padding:20px;
            border-radius:15px;
            text-align:center;
            color:white;
            margin-bottom:20px;
        ">
            <h1>{st.session_state.title}</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.info("💡 Type **0** to return to the Home Page.")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("🏠 Back to Home", use_container_width=True):
            go_home()

    with col2:
        if st.button("🗑️ Clear Chat", use_container_width=True):
            system_message = st.session_state.messages[0]
            st.session_state.messages = [system_message]
            st.rerun()

    st.markdown("---")

    # Display Chat

    for msg in st.session_state.messages:

        if isinstance(msg, HumanMessage):
            with st.chat_message("user"):
                st.write(msg.content)

        elif isinstance(msg, AIMessage):
            with st.chat_message("assistant"):
                st.write(msg.content)

    # Chat Input

    prompt = st.chat_input("Type your message...")

    if prompt:

        # Return Home

        if prompt.strip() == "0":
            go_home()

        # Show User Message

        with st.chat_message("user"):
            st.write(prompt)

        st.session_state.messages.append(
            HumanMessage(content=prompt)
        )

        # AI Response

        response = model.invoke(st.session_state.messages)

        st.session_state.messages.append(
            AIMessage(content=response.content)
        )

        with st.chat_message("assistant"):
            st.write(response.content)