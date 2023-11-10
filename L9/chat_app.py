"""
Chat Version 3
    ✅ Chat User and Assistant
    ✅ History (all messages)
    ✅ Animation when displaying the assistant message

"""

import random
import time
import streamlit as st
from chat_bot import ChatBotStatic, ChatBotRandom


# [i]                                                                                            #
# [i] Initialize FrontEnd App                                                                    #
# [i]                                                                                            #

def initialize() -> None:
    """
    Initialize the app
    """
    st.title("Simple chat (v3)")

    if "chatbot" not in st.session_state:
        st.session_state.chatbot = ChatBotStatic()


# [i]                                                                                            #
# [i] Display History Message                                                                    #
# [i]                                                                                            #

def display_history_messages():
    # Display chat messages from history on app rerun
    for message in st.session_state.chatbot.memory:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])


# [i]                                                                                            #
# [i] Display User Message                                                                       #
# [i]                                                                                            #

def display_user_msg(message: str):
    """
    Display user message in chat message container
    """
    st.session_state.chatbot.memory.append(
        {"role": "user", "content": message}
    )

    with st.chat_message("user", avatar="😎"):
        st.markdown(message)


# [i]                                                                                            #
# [i] Display User Message                                                                       #
# [i]                                                                                            #

def display_assistant_msg(message: str):
    """
    Display assistant message
    """
    with st.chat_message("assistant", avatar="🤖"):
        message_placeholder = st.empty()

        # Simulate stream of response with milliseconds delay
        full_response = ""
        for chunk in message.split():
            full_response += chunk + " "
            time.sleep(0.05)

            # Add a blinking cursor to simulate typing
            message_placeholder.markdown(full_response + "▌")

        message_placeholder.markdown(full_response)

        st.session_state.chatbot.memory.append(
            {"role": "assistant", "content": full_response}
        )


# [*]                                                                                            #
# [*] MAIN                                                                                       #
# [*]                                                                                            #

if __name__ == "__main__":
    initialize()

    # [i] Display History #
    display_history_messages()

    if prompt := st.chat_input("Type your request..."):

        # [*] Request & Response #
        display_user_msg(message=prompt)
        assistant_response = st.session_state.chatbot.generate_response(
            message=prompt
        )
        display_assistant_msg(message=assistant_response)

    # [i] Sidebar #
    with st.sidebar:
        st.write(st.session_state.chatbot.memory)
