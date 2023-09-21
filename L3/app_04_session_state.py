
"""
A simple Streamlit app that demonstrates the use of session state.

This app features a counter that increases when a button is clicked,
and the counter value is stored in the session state to persist
across user interactions. It also provides a button to reset the counter.

Usage:
    1. Run the Streamlit app with `streamlit run filename.py`
    2. Click the "Increment Counter" button to increase the counter.
    3. Click the "Reset Counter" button to reset the counter to zero.

Run this script using the following command:
   $ streamlit run [path/filename].py

    [>] To run this file, in your terminal, the root folder :
    (>) $ streamlit run L3/app_04_session_state.py

[*]                                                                                            [*]
[*] Capstone Project                                                                           [*]
[*]                                                                                            [*]
[@] Tutorial | Concepts:
Author: Fernando A J Peres
Date: 2023
"""

import streamlit as st
ABOUT_SESSION_STATE = """
# Session state

Session state in Streamlit is a powerful feature that allows you to store and access data that persists throughout a user's interaction with your app. Unlike regular variables in Python, session state variables are unique to each user and can be used to remember user-specific information, selections, or settings during their session.

Streamlit provides a special object called st.session_state that you can use to create and manage session state variables. These variables can be accessed and modified across different functions and interactions within your Streamlit app.

```python
st.session_state["my_key"]

# or

st.session_state.my_key
```

"""


# Streamlit app title
st.title('Session State Example')


# Initialize session state
if 'counter' not in st.session_state:
    st.session_state["counter"] = 0

# Buttons
increment_btn = st.button('Increment Counter')
reset_btn = st.button('Reset Counter')


# if ... increment the counter
if increment_btn:
    st.session_state.counter += 1

# if ... reset the counter
if reset_btn:
    st.session_state.counter = 0


# [@] the order is important:

# Display the current counter value
st.write(f'Current Counter Value: {st.session_state.counter}')

with st.expander("About Session-state"):
    st.markdown(ABOUT_SESSION_STATE)

with st.expander("Session-state (Memory)"):
    st.write(st.session_state)


CODE = """

import streamlit as st


# Streamlit app title
st.title('Session State Example')


# Initialize session state
if 'counter' not in st.session_state:
    st.session_state["counter"] = 0

# Buttons
increment_btn = st.button('Increment Counter')
reset_btn = st.button('Reset Counter')


# if ... increment the counter
if increment_btn:
    st.session_state.counter += 1

# if ... reset the counter
if reset_btn:
    st.session_state.counter = 0

"""
with st.expander("Code"):
    st.code(CODE)
