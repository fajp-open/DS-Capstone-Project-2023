"""
Chat
"""

import streamlit as st

from chat_bot import ChatBotStatic


def initialize() -> None:
    """
    Initialize the app
    """
    st.title("Simple chat (v0)")
    st.session_state.chatbot = ChatBotStatic()


# [i]                                                                                            #
# [i] Display User Message                                                                       #
# [i]                                                                                            #

def display_user_msg(message: str):
    """
    Display user message in chat message container
    """
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

        message_placeholder.markdown(message)


# [*]                                                                                            #
# [*] MAIN                                                                                       #
# [*]                                                                                            #

if __name__ == "__main__":

    initialize()

    if prompt := st.chat_input("Type your request..."):

        # [*] Request & Response #
        display_user_msg(message=prompt)
        assistant_response = st.session_state.chatbot.generate_response()
        display_assistant_msg(message=assistant_response)
