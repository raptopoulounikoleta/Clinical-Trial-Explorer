import streamlit as st
import pandas as pd

# 1. App Title & Layout
st.set_page_config(page_title="Clinical Trial Dashboard", layout="wide")
st.title("Clinical Trial Dashboard")

# ==========================================
# NEW: FILE UPLOADER
# ==========================================
st.sidebar.header("📂 Upload Data")
# This creates the drag & drop area in the sidebar
uploaded_file = st.sidebar.file_uploader("Upload your own CSV file", type=["csv"])

# 2. Read the data (Dynamic)
if uploaded_file is not None:
    # If user uploads a file, read that file
    my_data = pd.read_csv(uploaded_file)
    st.sidebar.success("File successfully uploaded!")
else:
    # If no file is uploaded, use the default local file
    my_data = pd.read_csv("patients_data.csv")
    st.sidebar.info("Using default patient data. Upload a file to replace it.")

# ==========================================
# PROFESSIONAL SIDEBAR (Filters)
# ==========================================
st.sidebar.header("⚙️ Filter Data")

# Safety Check: Make sure the required columns exist
if 'Age' in my_data.columns and 'Treatment' in my_data.columns:
    
    # Filter 1 (Slider) - Now dynamic based on the data!
    min_age = int(my_data['Age'].min())
    max_age = int(my_data['Age'].max())
    selected_age = st.sidebar.slider("Minimum Patient Age:", min_value=min_age, max_value=max_age, value=min_age)

    # Filter 2 (Multiselect)
    treatment_options = my_data['Treatment'].unique()
    selected_treatments = st.sidebar.multiselect(
        "Select Treatment Groups:",
        options=treatment_options,
        default=treatment_options
    )

    # Apply the filters
    condition = (my_data['Age'] >= selected_age) & (my_data['Treatment'].isin(selected_treatments))
    filtered_data = my_data[condition]

    # ==========================================
    # MAIN PAGE: VISUALIZATION & KPIs
    # ==========================================
    st.header("📊 Trial Overview")

    col1, col2, col3 = st.columns(3)

    total_patients = len(filtered_data)
    avg_age = round(filtered_data['Age'].mean(), 1) if not filtered_data.empty else 0
    total_treatments = filtered_data['Treatment'].nunique()

    col1.metric("Total Patients", total_patients)
    col2.metric("Average Age", f"{avg_age} yrs")
    col3.metric("Treatment Groups", total_treatments)

    st.divider()

    st.subheader("Patient Distribution by Treatment")
    if not filtered_data.empty:
        treatment_counts = filtered_data['Treatment'].value_counts()
        st.bar_chart(treatment_counts)
    else:
        st.warning("No data matches the selected filters.")

    st.divider()

    # ==========================================
    # RAW DATA TABLE
    # ==========================================
    st.subheader("Explore Patient Data")
    st.dataframe(filtered_data)
else:
    # Error message if the uploaded CSV is wrong
    st.error("The uploaded CSV must contain 'Age' and 'Treatment' columns to work with this dashboard.")