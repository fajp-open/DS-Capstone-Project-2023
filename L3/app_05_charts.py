"""
A Streamlit app demonstrating various types of charts using a toy sales dataset.

This Streamlit app showcases different chart types, including bar charts, line charts,
area charts, scatter plots, and a pie chart, to visualize the sales data of three products
(Product A, B, and C) over six months (Jan to Jun).

Usage:
    1. Run the Streamlit app with `streamlit run filename.py`.
    2. Explore the different chart types to visualize the toy sales dataset.

Run this script using the following command:
   $ streamlit run [path/filename].py

    [>] To run this file, in your terminal, the root folder :
    (>) $ streamlit run L3/app_05_charts.py
"""

import streamlit as st
import pandas as pd

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
st.title('Exploring Different Types of Charts')

# Display the dataset
st.subheader('Toy Sales Dataset')
st.dataframe(df)

# Bar chart
st.subheader('Bar Chart: Monthly Product Sales')
selected_product_bar = st.selectbox(
    "Select a product", ['ProductA_Sales', 'ProductB_Sales', 'ProductC_Sales'])
bar_chart_data = df[['Month', selected_product_bar]]
st.bar_chart(bar_chart_data.set_index('Month'))

# [@] KEY for similar components

# Line chart
st.subheader('Line Chart: Monthly Product Sales Over Time')
selected_products_line = st.multiselect("Select products to compare", [
                                        'ProductA_Sales', 'ProductB_Sales', 'ProductC_Sales'], key="multiselect_line")
line_chart_data = df[['Month'] + selected_products_line]
st.line_chart(line_chart_data.set_index('Month'))

# Area chart
st.subheader('Area Chart: Monthly Product Sales Over Time')
selected_products_area = st.multiselect("Select products to compare", [
                                        'ProductA_Sales', 'ProductB_Sales', 'ProductC_Sales'], key="multiselect_area")
area_chart_data = df[['Month'] + selected_products_area]
st.area_chart(area_chart_data.set_index('Month'))
st.plotly_chart