# 🌾 FAO Global Food Production Analysis

This project provides a comprehensive exploratory data analysis (EDA) of global food production using data from the **Food and Agriculture Organization (FAO)** of the United Nations. It explores patterns, trends, and insights into food produced for **human consumption** and **animal feed** across countries and decades.

## 📌 Project Goals

- Understand the global distribution of food production
- Compare production for human consumption vs. animal feed
- Visualize trends by country, item, and year
- Identify key contributors to global food output
- Provide an interactive dashboard *(optional via Streamlit)*

---

## 📂 Dataset

- **Source**: [FAO Food Balance Sheets](https://www.fao.org/faostat/)
- **File**: `FAO.csv`
- **Attributes**:
  - `Area`, `Item`, `Element` (Food or Feed)
  - `Year`, `Value` (Production Quantity)
  - Country codes, geographic data, etc.

---

## 📊 Visualizations Included

- Top countries by food/feed production
- Trends over time (1961 onwards)
- Comparison of food vs feed production by country
- Heatmaps, bar charts, and line plots for insights
- *(Optional)* Interactive Streamlit dashboard

---

## 🛠️ Technologies Used

- **Python 3**
- **Pandas**, **NumPy** – Data manipulation  
- **Matplotlib**, **Seaborn**, **Plotly** – Visualization  
- **Streamlit** *(optional)* – Dashboard app  
- **Google Colab** – EDA notebook environment  

---

## 🚀 How to Run

### 🔍 EDA (Colab/Jupyter Notebook)
1. Clone the repository  
   ```bash
   git clone https://github.com/yourusername/fao-global-food-analysis.git
   cd fao-global-food-analysis
