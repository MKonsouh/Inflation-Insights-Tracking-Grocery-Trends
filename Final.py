import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
import numpy as np

# Apply a consistent theme for the plots
sns.set_theme(style="whitegrid")

# Load the cleaned datasets
milk_data = pd.read_csv("milk_data_cleaned.csv")
bread_data = pd.read_csv("bread_data_cleaned.csv")
flour_data = pd.read_csv("flour_data_cleaned.csv")
eggs_data = pd.read_csv("eggs_data_cleaned.csv")

# Convert 'Date' column to datetime
milk_data['Date'] = pd.to_datetime(milk_data['Date'])
bread_data['Date'] = pd.to_datetime(bread_data['Date'])
flour_data['Date'] = pd.to_datetime(flour_data['Date'])
eggs_data['Date'] = pd.to_datetime(eggs_data['Date'])

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Select Page", ["Overview", "Milk", "Bread", "Flour", "Eggs"])

# Sidebar filters
st.sidebar.subheader("Filters")
start_date = st.sidebar.date_input("Start Date", milk_data['Date'].min())
end_date = st.sidebar.date_input("End Date", milk_data['Date'].max())
selected_items = st.sidebar.multiselect(
    "Select Items for Combined Trends",
    ["Milk", "Bread", "Flour", "Eggs"],
    default=["Milk", "Bread", "Flour", "Eggs"]
)

# Filter data based on date range
def filter_data(data):
    return data[(data['Date'] >= pd.Timestamp(start_date)) & (data['Date'] <= pd.Timestamp(end_date))]

milk_data_filtered = filter_data(milk_data)
bread_data_filtered = filter_data(bread_data)
flour_data_filtered = filter_data(flour_data)
eggs_data_filtered = filter_data(eggs_data)

# Helper function for insights
def calculate_insights(data, price_column):
    latest_price = data[price_column].iloc[-1]
    avg_price = data[price_column].mean()
    change_pct = ((latest_price - data[price_column].iloc[0]) / data[price_column].iloc[0]) * 100
    return latest_price, avg_price, change_pct

# Helper function for trend prediction
def predict_trend(data, price_column):
    data['Timestamp'] = data['Date'].map(pd.Timestamp.timestamp)
    X = np.array(data['Timestamp']).reshape(-1, 1)
    y = data[price_column]
    model = LinearRegression().fit(X, y)
    predictions = model.predict(X)
    data['Trend'] = predictions
    return data, model.coef_[0]  # Returns data with predictions and the slope

if page == "Overview":
    st.title("Grocery Store Price Trends: Milk, Bread, Flour, and Eggs")
    st.write(
        "Insights into the price trends of milk, bread, flour, and eggs "
        "from 2020 to the present."
    )

    # Display combined trends
    st.subheader("Combined Price Trends")
    fig_combined, ax_combined = plt.subplots(figsize=(10, 6))
    if "Milk" in selected_items:
        sns.lineplot(x="Date", y="Milk_Price", data=milk_data_filtered, marker="o", label="Milk", color="blue", ax=ax_combined)
    if "Bread" in selected_items:
        sns.lineplot(x="Date", y="Bread_Price", data=bread_data_filtered, marker="s", label="Bread", color="green", ax=ax_combined)
    if "Flour" in selected_items:
        sns.lineplot(x="Date", y="Flour_Price", data=flour_data_filtered, marker="^", label="Flour", color="red", ax=ax_combined)
    if "Eggs" in selected_items:
        sns.lineplot(x="Date", y="Eggs_Price", data=eggs_data_filtered, marker="x", label="Eggs", color="purple", ax=ax_combined)
    ax_combined.set_title("Combined Price Trends", fontsize=16, weight='bold')
    st.pyplot(fig_combined)

elif page in ["Milk", "Bread", "Flour", "Eggs"]:
    st.title(f"{page} Price Insights")

    # Select data and columns based on the page
    if page == "Milk":
        data = milk_data_filtered
        price_column = "Milk_Price"
        color = "blue"
    elif page == "Bread":
        data = bread_data_filtered
        price_column = "Bread_Price"
        color = "green"
    elif page == "Flour":
        data = flour_data_filtered
        price_column = "Flour_Price"
        color = "red"
    else:  # Eggs
        data = eggs_data_filtered
        price_column = "Eggs_Price"
        color = "purple"

    # Calculate insights
    latest_price, avg_price, change_pct = calculate_insights(data, price_column)

    # Ensure predictions are applied to the dataset
    data, slope = predict_trend(data, price_column)

    # Layout: columns for graph and insights
    col1, col2 = st.columns([3, 1])  # 3:1 ratio for graph and insights
    with col1:
        st.subheader(f"{page} Price Trend")
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.lineplot(x="Date", y=price_column, data=data, color=color, marker="o", label="Actual Prices", ax=ax)
        sns.lineplot(x="Date", y="Trend", data=data, color="orange", label="Trend", ax=ax)
        ax.set_title(f"{page} Price Trend", fontsize=16, weight='bold')
        ax.set_xlabel("Date", fontsize=12)
        ax.set_ylabel("Price (USD)", fontsize=12)
        ax.legend(fontsize=10)
        ax.grid(visible=True, linestyle="--", alpha=0.5)
        st.pyplot(fig)

    with col2:
        st.subheader("Insights")
        st.metric("Latest Price", f"${latest_price:.2f}")
        st.metric("Average Price", f"${avg_price:.2f}")
        st.metric("Change Since 2020", f"{change_pct:.2f}%")
