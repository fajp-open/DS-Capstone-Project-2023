"""
Chat
"""

import time
import streamlit as st
from chat_bot import ChatBotStatic


# [i]                                                                                            #
# [i] Initialize FrontEnd App                                                                    #
# [i]                                                                                            #

def initialize() -> None:
    """
    Initialize the app
    """
    st.title("Simple chat (v1)")
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

        # Simulate stream of response with milliseconds delay
        full_response = ""
        for chunk in message.split():
            full_response += chunk + " "
            time.sleep(0.05)

            # Add a blinking cursor to simulate typing
            message_placeholder.markdown(full_response)# + "▌")

        message_placeholder.markdown(full_response)

# [*]                                                                                            #
# [*] MAIN                                                                                       #
# [*]                                                                                            #


if __name__ == "__main__":
    initialize()

    # [*] Request & Response #
    if prompt := st.chat_input("Type your request..."):
        display_user_msg(message=prompt)
        assistant_response = st.session_state.chatbot.generate_response()
        display_assistant_msg(message=assistant_response)
