def format_chat_as_text(chat_ui):
    chat_text = ""
    for msg in chat_ui:
        role = "User" if msg["role"] == "user" else "AI"
        chat_text += f"{role}: {msg['content']}\n\n"
    return chat_text