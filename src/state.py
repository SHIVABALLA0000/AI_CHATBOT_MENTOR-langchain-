import streamlit as st

def init_state():
    if "selected_module" not in st.session_state:
        st.session_state.selected_module = None

    if "chat_ui" not in st.session_state:
        st.session_state.chat_ui = []

    if "messages" not in st.session_state:
        st.session_state.messages = []