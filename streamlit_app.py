import streamlit as st
import pandas as pd
import plotly.express as px
import io
import datetime

# --- Helper Functions ---
def load_data():
    """Loads data for categories and monthly transactions."""
    return {
        "categories": {
            "categories": [
                {"name": "Categories", "amount": 130000000, "description": "Total Amount"},
            ]
        },
        "monthly": {
            "categories": [
                {"name": "Category", "amount": 10000, "description": "Total Amount"},
            ]
        },
    }

# --- Streamlit App ---
st.set_page_config(
    layout="wide",  # Enhance layout
    title="ČSOB Finance Dashboard",
    icon="💰",
)

# --- Navigation ---
st.sidebar.header("Navigation")
st.sidebar.subheader("Main Navigation")
st.radio("Select View", ["Dashboard", "Transactions", "Categories", "Account Overview", "Import Data"])

# --- Main Content ---
# --- Dashboard Section ---
if st.sidebar.radio("Dashboard", ["Dashboard", "Transactions", "Categories", "Account Overview", "Import Data"]):
    st.header("Dashboard")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Total Amount", 1234567890)
    with col2:
        st.metric("Total Transactions", 12345)
    with col3:
        st.metric("Average Monthly", 1234567890)
    with col4:
        st.metric("Total Expenses", 1234567890)

    st.subheader("Monthly Overview")
    fig = px.bar(data_frame=pd.DataFrame({
        "month": [f"{d.strftime('%B')}" for d in range(1, 12)],
        "amount": 1234567890
    }))
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Top Categories")
    fig_top = px.bar(data_frame=pd.DataFrame({
        "category": ["Category 1", "Category 2", "Category 3"],
        "amount": 1234567890
    }))
    st.plotly_chart(fig_top, use_container_width=True)

    st.subheader("Total Expenses")
    st.metric("Total Expenses", 1234567890, label="Total")
    st.metric("Total Income", 1234567890, label="Total")

    st.subheader("Top Categories")
    st.bar(data=pd.DataFrame({
        "category": ["Category 1", "Category 2", "Category 3"],
        "amount": 1234567890
    }))
    st.bar(data=pd.DataFrame({
        "category": ["Category 1", "Category 2", "Category 3"],
        "amount": 1234567890
    }))

# --- Transactions Section ---
elif st.sidebar.radio("Transactions", ["Dashboard", "Transactions", "Categories", "Account Overview", "Import Data"]):
    st.header("Transactions")

    st.subheader("Recent Transactions")
    st.dataframe(df_transactions)  # Replace with actual data

# --- Categories Section ---
elif st.sidebar.radio("Categories", ["Dashboard", "Transactions", "Categories", "Account Overview", "Import Data"]):
    st.header("Categories")

    st.subheader("Category Overview")
    categories_data = load_data()['categories']['categories']
    st.dataframe(categories_data)

# --- Import Data Section ---
elif st.sidebar.radio("Import Data", ["Dashboard", "Transactions", "Categories", "Account Overview", "Import Data"]):
    st.header("Import Data")

    st.subheader("Upload CSV File")
    uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

    if uploaded_file is None:
        st.warning("Please upload a CSV file.")
    elif uploaded_file:
        try:
            df = pd.read_csv(uploaded_file)
            st.success("Data imported successfully!")
            st.dataframe(df)
        except Exception as e:
            st.error(f"Error importing data: {e}")

# --- Placeholder for future enhancements (optional) ---
# You can add a section to display a chart of account activity.
# Or a section to show a list of transactions with filtering options.

# --- Export to GitHub ---
# To export this code to GitHub, you can simply create a new repository
# and commit the code to it.

# --- Deploy to Streamlit.io ---
# To deploy to Streamlit.io, you can follow these steps:
# 1. Create a new app on Streamlit.io: [https://streamlit.io/create-an-app](https://streamlit.io.io/create-an-app)
# 2. Paste the code into the code editor.
# 3. Click the "Deploy" button.
