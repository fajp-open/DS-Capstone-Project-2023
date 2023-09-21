"""
Streamlit Tutorial with Sidebar and Widgets

This Python script serves as a beginner-friendly tutorial for creating interactive web applications using Streamlit. It demonstrates the use of Streamlit's sidebar and various widgets, such as text input, selectbox, checkbox, slider, button, radio, date input, and time input.

Usage:
1. Make sure you have Streamlit installed. You can install it using 'pip install streamlit'.

2. Run this script using the following command:
   $ streamlit run [path/filename].py

    [>] To run this file, in your terminal, the root folder :
    (>) $ streamlit run L3/app_03_sidebar.py

3. After running the command, a local development server will start, and your default web browser will open with the Streamlit app.

4. Interact with the sidebar widgets to see how they affect the main content area.

5. Explore, modify, and expand upon this example to create your own Streamlit apps.



[*]                                                                                            [*]
[*] Capstone Project                                                                           [*]
[*]                                                                                            [*]
[@] Tutorial | Concepts:
Author: Fernando A J Peres
Date: 2023
"""

# Import the Streamlit library
import datetime
import streamlit as st

# Create a title for your app
st.title("Streamlit Tutorial with Sidebar")

# Add text to the main content area
st.write("Welcome to this Streamlit tutorial. You can use the sidebar to interact with the app.")

# Create a sidebar using st.sidebar
st.sidebar.title("Sidebar Options")

# Add widgets to the sidebar

# Text Input Widget
# Create a text input box
user_input = st.text_input("Enter your name", "Your Name")
# Display a greeting message based on the input
st.write("Hello,", user_input, "!")

# Selectbox Widget
option = st.sidebar.selectbox("Choose an option", [
                              "Option 1", "Option 2", "Option 3"])  # Create a dropdown select box
st.sidebar.write("You selected:", option)  # Display the selected option

# Checkbox Widget
if st.sidebar.checkbox("Show/hide content"):  # Create a checkbox
    # Display or hide content based on checkbox state
    st.write("You can now see or hide this content.")

# Slider Widget
slider_value = st.sidebar.slider(
    "Select a value", 1, 100, 50)  # Create a slider
# Display the selected slider value
st.sidebar.write("You selected:", slider_value)

# Radio Widget
# Create a radio button group
radio_choice = st.sidebar.radio("Choose one", ["A", "B", "C"])
# Display the selected radio button choice
st.sidebar.write("You chose:", radio_choice)

# Date Input Widget
date_input = st.sidebar.date_input(
    "Pick a date", datetime.date(2023, 1, 1))  # Create a date input field
st.sidebar.write("Selected date:", date_input)  # Display the selected date

# Time Input Widget
time_input = st.sidebar.time_input(
    "Set a time", datetime.time(12, 00))  # Create a time input field
st.sidebar.write("Selected time:", time_input)  # Display the selected time

# Button Widget
if st.button("Click me"):  # Create a button
    st.write("Button clicked!")  # Display a message when the button is clicked
