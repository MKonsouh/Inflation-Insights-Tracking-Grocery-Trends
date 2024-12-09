📊 Inflation Insights: Tracking Grocery Trends
Inflation Insights is a Streamlit app that analyzes grocery price trends for key staples like milk, bread, flour, and eggs. By leveraging data from the U.S. Bureau of Labor Statistics (BLS), this app explores the relationship between grocery prices and inflation, providing interactive visualizations and actionable insights.
[![Open App](https://img.shields.io/badge/Launch_App-Streamlit-orange)](https://inflation-insights-tracking-grocery-trends-ts6nartdbxbstgl24g7.streamlit.app/)


🌟 Key Features:
Visualize Price Trends: Explore how prices for essential groceries have changed over time.
Inflation Correlation: Analyze the relationship between grocery price trends and broader inflation metrics.
Interactive Insights: Dive into the data with interactive charts and tools.


⚙️ Data Operation and Abstraction Design
This project employs a robust data operation and abstraction design to ensure efficient handling of grocery price data from the BLS.

Data Acquisition
Source: Data is retrieved from the U.S. Bureau of Labor Statistics (BLS) using the BLS Public Data API.
API Registration: An API key is used to access detailed historical time series data.
Series Identification: The specific BLS series IDs for grocery staples (milk, bread, flour, and eggs) are used to fetch relevant data.
