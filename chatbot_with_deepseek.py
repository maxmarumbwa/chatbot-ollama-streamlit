import streamlit as st
from ollama import chat  # Ollama function

st.title("Your DeepSeek Chatbot (Ollama Local)")

MODEL = "deepseek-r1:1.5b"

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Get user input
if prompt := st.chat_input("What's up?"):

    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate assistant reply using Ollama
    response = chat(model=MODEL, messages=st.session_state.messages)

    # ✅ Access the assistant reply
    assistant_reply = response.text

    # Display assistant reply
    with st.chat_message("assistant"):
        st.markdown(assistant_reply)

    # Add assistant reply to chat history
    st.session_state.messages.append({"role": "assistant", "content": assistant_reply})
