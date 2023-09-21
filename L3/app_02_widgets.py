"""
[*]                                                                                            [*]
[*] Capstone Project                                                                           [*]
[*]                                                                                            [*]
[@] Tutorial | Concepts:

Streamlit Hello World with Widgets
----------------------------------

This Python script demonstrates the use of Streamlit to create a simple "Hello World" web app with a sidebar and interactive widgets.

It showcases the following components:

- A main content area with a header displaying "Hello world!"
- A sidebar with a title "Hello world from side bar."

Widgets:
1. Text Input: Allows users to input their name, with a default value of "Your Name."
2. Button: A button labeled "Click me" that, when clicked, displays a message.
3. Selectbox: A dropdown menu with options "Option 1," "Option 2," and "Option 3."


To run this script, make sure you have Streamlit installed and use the command:

$ streamlit run [path/filename].py

[>] To run this file, in your terminal, the root folder :
(>) $ streamlit run L3/app_02_widgets.py

Author: Fernando A J Peres
Date: 2023
"""

import streamlit as st

# hello
# ------------------------------------------------------------------------------------------------
st.header("Hello world!")

with st.sidebar:
    st.title("Hello world from side bar")

# widgets
# ------------------------------------------------------------------------------------------------

# input
user_input = st.text_input("Enter your name", "Your Name")
st.write("You entered:", user_input)

# button
btn = st.button("Click me")
if btn:
    st.write("Button clicked!")

# select box
option = st.selectbox("Choose an option", ["Option 1", "Option 2", "Option 3"])
st.write("You selected:", option)