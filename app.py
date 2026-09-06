import streamlit as st
import pandas as pd

# App title
st.title("Clinical Trial Dashboard")

# Read the data
my_data = pd.read_csv("patients_data.csv")

# Interactive tool (Slider)
selected_age = st.slider("Minimum Patient Age:", min_value=18, max_value=100, value=50)

# Custom logic (Data Wrangling)
condition = (my_data['Treatment'] == 'Drug') & (my_data['Age'] > selected_age)

# Filter and display on screen
filtered_patients = my_data[condition]
st.dataframe(filtered_patients)
