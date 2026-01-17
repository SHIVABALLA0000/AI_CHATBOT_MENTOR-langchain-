import streamlit as st
from dotenv import load_dotenv
import os

from src.llm import get_llm
from src.prompts import get_system_prompt
from src.state import init_state
from src.chat import format_chat_as_text

# =========================
# Environment
# =========================
load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("gemini")

# =========================
# Page config
# =========================
st.set_page_config(
    page_title="AI Chatbot Mentor",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 AI Chatbot Mentor")
st.caption("Domain-Specific Intelligent Learning Assistant")

# =========================
# Modules
# =========================
MODULES = [
    "Python",
    "SQL",
    "Power BI",
    "Exploratory Data Analysis (EDA)",
    "Machine Learning (ML)",
    "Deep Learning (DL)",
    "Generative AI (Gen AI)",
    "Agentic AI"
]

# =========================
# Init State
# =========================
init_state()

# =========================
# Module Selection
# =========================
if st.session_state.selected_module is None:
    st.markdown("### 👋 Welcome to AI Chatbot Mentor")
    module = st.selectbox("📌 Select a Module", MODULES)

    if st.button("Start Mentoring"):
        st.session_state.selected_module = module
        st.session_state.chat_ui = []
        st.session_state.messages = [
            ("system", get_system_prompt(module))
        ]
        st.rerun()

# =========================
# Mentor Screen
# =========================
else:
    module = st.session_state.selected_module
    st.subheader(f"Welcome to {module} AI Mentor 🎯")

    with st.sidebar:
        st.subheader("⚙️ Controls")

        if st.button("🔁 Change Module"):
            st.session_state.selected_module = None
            st.session_state.chat_ui = []
            st.session_state.messages = []
            st.rerun()

        if st.button("🧹 Clear Chat"):
            st.session_state.chat_ui = []
            st.session_state.messages = [
                st.session_state.messages[0]
            ]
            st.rerun()

        st.download_button(
            "📥 Download Chat",
            data=format_chat_as_text(st.session_state.chat_ui),
            file_name=f"{module}_chat.txt",
            mime="text/plain",
            disabled=len(st.session_state.chat_ui) == 0
        )

    for msg in st.session_state.chat_ui:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    user_input = st.chat_input("Ask your question...")

    if user_input:
        st.session_state.chat_ui.append(
            {"role": "user", "content": user_input}
        )
        st.session_state.messages.append(("user", user_input))

        llm = get_llm()
        response = llm.invoke(st.session_state.messages)

        with st.chat_message("assistant"):
            st.write(response.content)

        st.session_state.chat_ui.append(
            {"role": "assistant", "content": response.content}
        )
        st.session_state.messages.append(("assistant", response.content))