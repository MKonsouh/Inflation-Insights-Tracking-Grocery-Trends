# 📊 Inflation Insights: Tracking Grocery Trends  

**Inflation Insights** is a Streamlit app that analyzes grocery price trends for key staples like milk, bread, flour, and eggs. Using data from the U.S. Bureau of Labor Statistics (BLS), it provides interactive visualizations and insights to explore the relationship between grocery prices and inflation.

[![Open App](https://img.shields.io/badge/Launch_App-Streamlit-orange)](https://inflation-insights-tracking-grocery-trends-ts6nartdbxbstgl24g7.streamlit.app/)

---

## 🌟 Key Features  
- **Visualize Price Trends**: See how prices for essential groceries have changed over time.  
- **Inflation Correlation**: Analyze the relationship between grocery prices and inflation.  
- **Interactive Insights**: Use dynamic charts and tools to explore the data.

---

## ⚙️ Data Workflow  

This project uses a structured data operation and abstraction design to handle data efficiently:

### Data Acquisition  
- Data is retrieved from the [BLS Public Data API](https://www.bls.gov/developers/home.htm).  
- An API key is used to access detailed historical data.  
- Specific BLS series IDs are used for staples like milk, bread, flour, and eggs.

### Data Transformation  
- Data is normalized into consistent units for analysis.  
- Missing values are addressed through interpolation or exclusion.  
- Time series data is aligned for accurate comparisons.

### Integration and Analysis  
- A modular design simplifies data retrieval and preparation.  
- The app dynamically fetches and visualizes the data using Streamlit.

---

With its intuitive design and robust data foundation, **Inflation Insights** makes it easy to understand the impact of inflation on everyday groceries.  

[Launch the App](https://inflation-insights-tracking-grocery-trends-ts6nartdbxbstgl24g7.streamlit.app/)

---
