"""
[*]                                                                                            [*]
[*] Capstone Project                                                                           [*]
[*]                                                                                            [*]
[@] Tutorial | Concepts:

This Python script showcases a simple "Hello World" example using the Streamlit package. Streamlit is a Python library that allows you to create interactive web applications with minimal code.

The main content of the web app displays a header with the text "Hello world!" in the center. Additionally, there is a sidebar with a title "Hello world from side bar."

To run this script, make sure you have Streamlit installed and use the command:

$ streamlit run [path/filename].py

[>] To run this file, in your terminal, the root folder :
(>) $ streamlit run L3/app_01_hello_world.py

Author: Fernando A J Peres
Date: 2023
"""

import streamlit as st

st.header("Hello world!")

with st.sidebar:
    st.title("Hello world from side bar")