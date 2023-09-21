
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

# Create a toy dataset
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'ProductA_Sales': [2500, 3200, 2800, 4500, 3800, 4200],
    'ProductB_Sales': [1800, 2100, 1700, 2900, 2500, 3000],
    'ProductC_Sales': [3500, 4200, 3800, 5500, 4800, 5100]
}

# Convert the dictionary to a DataFrame
df = pd.DataFrame(data)

# Streamlit app title
st.title('Simple Chart Examples')

# Option to select the chart type
with st.sidebar:
    chart_type = st.radio("Select a chart type:", ('Matplotlib', 'Plotly'))

# Display the dataset
st.subheader('Toy Sales Dataset')
st.dataframe(df)

# Generate the chart based on the selected chart_type
if chart_type == 'Matplotlib':
    st.subheader('Matplotlib Bar Chart')
    selected_product_bar = st.selectbox(
        "Select a product",
        ['ProductA_Sales', 'ProductB_Sales', 'ProductC_Sales'],
    )

    fig, ax = plt.subplots()
    ax.bar(df['Month'], df[selected_product_bar])
    ax.set_xlabel('Month')
    ax.set_ylabel('Sales')
    st.pyplot(fig)

elif chart_type == 'Plotly':
    st.subheader('Plotly Line Chart')
    selected_products_line = st.multiselect(
        "Select products to compare",
        ['ProductA_Sales', 'ProductB_Sales', 'ProductC_Sales'],
        default=['ProductA_Sales']
    )

    fig = px.line(
        df,
        x='Month',
        y=selected_products_line,
        title='Monthly Product Sales'
    )

    st.plotly_chart(fig)
