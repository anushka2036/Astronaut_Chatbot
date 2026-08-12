import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, AIMessage

st.title("Chatbot")

# initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# display chat messages from history on app rerun
for message in st.session_state.messages:
    if isinstance(message, HumanMessage):
        with st.chat_message("user"):
            st.markdown(message.content)

    elif isinstance(message, AIMessage):
        with st.chat_message("assistant"):
            st.markdown(message.content)

# user input
prompt = st.chat_input("How can I help you?")

if prompt:

    # show user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # store user message
    st.session_state.messages.append(
        HumanMessage(content=prompt)
    )

    # load model
    llm = ChatOllama(
        model="llama3.2",
        temperature=0.7
    )

    # generate response
    result = llm.invoke(st.session_state.messages)

    # show assistant response
    with st.chat_message("assistant"):
        st.markdown(result.content)

    # store assistant response
    st.session_state.messages.append(
        AIMessage(content=result.content)
    )