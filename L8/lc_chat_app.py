"""
Chat
"""
import time
import streamlit as st

from chat_bot import ChatBotRandom  # ChatBotStatic

# [i]                                                                                            #
# [i] Initialize                                                                                 #
# [i]                                                                                            #


def initialize():
    st.title("ChatBot 1")
    if "chatbot" not in st.session_state:
        st.session_state.chatbot = ChatBotRandom()
        # chatBot = ChatBotStatic()


# [i]                                                                                            #
# [i] Display all messages                                                                       #
# [i]                                                                                            #

def display_history_messages():

    # {"role": "assistant", "content": message}

    for message in st.session_state.chatbot.memory:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# [i]                                                                                            #
# [i] Display User messages                                                                      #
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
# [i] Display Assistant Message                                                                  #
# [i]                                                                                            #


def display_assistant_msg(message: str):
    """
    Display user message in chat message container
    """
    with st.chat_message("assistant", avatar="🤖"):
        message_placeholder = st.empty()  # markdown(message)

    # animate
    full_response = ""
    for chunk in message.split():
        full_response += chunk + " "
        time.sleep(0.05)
        message_placeholder.markdown(full_response + "▌")

    message_placeholder.markdown(full_response)

    st.session_state.chatbot.memory.append(
        {"role": "assistant", "content": message}
    )

# [i]                                                                                            #
# [i] Main                                                                                       #
# [i]                                                                                            #


if __name__ == "__main__":
    # initialize
    initialize()

    # show all messages
    display_history_messages()

    if prompt := st.chat_input("Type your request..."):

        # user send a message and we display the message
        display_user_msg(message=prompt)

        # chatBot generates the response
        assistant_response = st.session_state.chatbot.generate_response(
            message=prompt)

        # Display chatBot response
        display_assistant_msg(message=assistant_response)

        # After all the chat interactions
        with st.sidebar:
            st.text("Memory")
            st.write(st.session_state.chatbot.memory)
