import streamlit as st
import mysql.connector
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

# -----------------------------
# MySQL Connection Configuration
# -----------------------------
def create_connection():
    return mysql.connector.connect(
        host="localhost",       # XAMPP MySQL host
        user="root",            # Default XAMPP user
        password="",            # Leave empty if no password
        database="s1_db"    # Your database name
    )

# -----------------------------
# Fetch Data from Database
# -----------------------------
@st.cache_data
def load_data():
    conn = create_connection()
    query = "SELECT * FROM sales_data"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# -----------------------------
# Streamlit UI
# -----------------------------
st.title("📊 MySQL Data Visualization Dashboard")
st.write("This app connects to XAMPP MySQL and visualizes the data interactively.")

# Load data
df = load_data()

st.subheader("Raw Data Preview")
st.dataframe(df)

# -----------------------------
# Filters
# -----------------------------
categories = df["category"].unique()
selected_category = st.multiselect("Filter by Category", categories, default=categories)

filtered_df = df[df["category"].isin(selected_category)]

# -----------------------------
# Graph Selection
# -----------------------------
chart_type = st.selectbox(
    "Select Chart Type",
    ["Bar Chart", "Line Chart", "Pie Chart", "Scatter Plot", "Histogram"]
)

st.subheader("📈 Visualization")

if chart_type == "Bar Chart":
    fig = px.bar(filtered_df, x="product_name", y="quantity", color="category",
                 title="Product Quantity by Category")
    st.plotly_chart(fig)

elif chart_type == "Line Chart":
    fig = px.line(filtered_df, x="sale_date", y="price", color="product_name",
                  title="Price Trend Over Time")
    st.plotly_chart(fig)

elif chart_type == "Pie Chart":
    fig = px.pie(filtered_df, values="quantity", names="category",
                 title="Sales Distribution by Category")
    st.plotly_chart(fig)

elif chart_type == "Scatter Plot":
    fig = px.scatter(filtered_df, x="quantity", y="price", color="category",
                     size="price", hover_name="product_name",
                     title="Quantity vs Price Scatter Plot")
    st.plotly_chart(fig)

elif chart_type == "Histogram":
    fig, ax = plt.subplots()
    ax.hist(filtered_df["price"], bins=10, edgecolor='black')
    ax.set_title("Price Distribution")
    ax.set_xlabel("Price")
    ax.set_ylabel("Frequency")
    st.pyplot(fig)

# -----------------------------
# Data Summary
# -----------------------------
st.subheader("📋 Data Summary")
st.write(filtered_df.describe())

