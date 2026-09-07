import streamlit as st
import pandas as pd

# 1. App Title
st.title("Clinical Trial Dashboard")

# 2. Read the data
my_data = pd.read_csv("patients_data.csv")

# ==========================================
# NEW SECTION: VISUALIZATION & KPIs
# ==========================================
st.header("📊 Trial Overview")

# Create 3 columns for our metrics
col1, col2, col3 = st.columns(3)

# Pandas calculations (using my_data)
total_patients = len(my_data)
avg_age = round(my_data['Age'].mean(), 1)
total_treatments = my_data['Treatment'].nunique()

# Display Metrics (KPIs)
col1.metric("Total Patients", total_patients)
col2.metric("Average Age", f"{avg_age} yrs")
col3.metric("Treatment Groups", total_treatments)

st.divider() # Adds a clean divider line

st.subheader("Patient Distribution by Treatment")
# Count treatments and create a Bar Chart
treatment_counts = my_data['Treatment'].value_counts()
st.bar_chart(treatment_counts)

st.divider() # Adds another divider line

# ==========================================
# OLD SECTION: FILTERS & TABLE
# ==========================================
st.subheader("Explore Patient Data")

# Interactive tool (Slider)
selected_age = st.slider("Minimum Patient Age:", min_value=18, max_value=100, value=50)

# Custom logic (Data Wrangling)
condition = (my_data['Treatment'] == 'Drug') & (my_data['Age'] > selected_age)

# Filter and display on screen
filtered_patients = my_data[condition]
st.dataframe(filtered_patients)
