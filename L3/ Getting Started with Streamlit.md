# Getting Started with Streamlit: Building Interactive Web Apps with Python

<br>

Streamlit is a Python library that makes it incredibly easy to create interactive web applications with just a few lines of code. In this tutorial, we'll explore the basics of Streamlit and build a simple interactive web app.

<br>

## Installation

To install Streamlit, open your terminal or command prompt and run the following command:

```bash
pip install streamlit
```

<br>

## Your First Streamlit App

Let's create a basic Streamlit app that displays "Hello, Streamlit!" in the browser.

<br>

### 1. Create a new Python script

| (e.g., `hello_streamlit.py`) and open it in your favorite code editor

<br>

### 2. Import

Import the Streamlit library at the top of your script

```python
import streamlit as st
```

<br>

### 3. Code

Add the following code to your script.

```python
# Header
st.header("Hello, Streamlit!")

with st.sidebar:
    st.title("Hello world from side bar")
```

<br>

### 4. Run

To run your Streamlit app, open your terminal, navigate to the directory where your script is located, and execute:

```bash
streamlit run hello_streamlit.py
```

| `streamlit run` [path/filename.py]

<br>

This will start a local development server and open your default web browser with your Streamlit app.

You should see a web page displaying "Hello, Streamlit!" in a large header.

<br>

---

<br>

## Adding Widgets

One of Streamlit's powerful features is its ability to easily integrate interactive widgets into your app. Let's add a few widgets to our app.

<br>

### Text Input

You can add a text input box using the `st.text_input()` function. Here's an example:

```python
user_input = st.text_input("Enter your name", "Your Name")
st.write("You entered:", user_input)
```

This code creates a text input box where users can enter their name. The default value is set to "Your Name." When users enter their name, it will be displayed below the input box.

<br>

### Button

You can add a button using the `st.button()` function. Here's an example:

```python
btn = st.button("Click me")
if btn:
    st.write("Button clicked!")
```

This code creates a button labeled "Click me." When users click the button, it will display "Button clicked!" below it.

<br>

### Selectbox

You can add a selectbox (dropdown menu) using the `st.selectbox()` function. Here's an example:

```python
option = st.selectbox("Choose an option", ["Option 1", "Option 2", "Option 3"])
st.write("You selected:", option)
```

This code creates a selectbox with three options. When users select an option, it will display their choice below the selectbox.

<br>

## Conclusion

Congratulations!

You've just built your first Streamlit app and added interactive widgets to it. Streamlit makes it easy to create powerful and interactive web applications using Python, making it a great choice for data visualization, prototyping, and more.

Explore Streamlit's documentation (<https://docs.streamlit.io/>) to discover even more features and capabilities. Happy coding!
