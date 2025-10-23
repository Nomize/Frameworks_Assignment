# Python Frameworks Assignment: CORD-19 Data Analysis & Streamlit App

Welcome to my **Python Frameworks Assignment!**  
This repository showcases my work analyzing the **CORD-19 research dataset**, focusing on data exploration, visualization, and the creation of an **interactive Streamlit web app** for insight discovery.

**🔗 Live App:** [View on Streamlit Cloud](https://nomize-frameworks-assignment-meta-cst38i.streamlit.app/)  
**📁 GitHub Repository:** [Nomize/Frameworks_Assignment](https://github.com/Nomize/Frameworks_Assignment.git)

---

## 📂 Repository Structure

Frameworks_Assignment/
├── data/
│ └── metadata_sample.csv # 2,000-row sample dataset for testing
├── meta.py # Streamlit app code
├── pyDA.py # Data processing script (used to create sample)
├── pyDA.ipynb # Jupyter Notebook for initial exploration
├── requirements.txt # Project dependencies for Streamlit Cloud
├── .gitignore # Ignores large files (metadata.csv, etc.)
└── README.md # Project documentation

pgsql
Copy code

> **Note:** The full `metadata.csv` (CORD-19) file is not included in the repo due to its large size (~2GB).  
> A smaller `metadata_sample.csv` file has been generated and is used for the Streamlit demo.

---

## 1️⃣ Project Overview

This project explores the **CORD-19 (COVID-19 Open Research Dataset)** and demonstrates key data analysis and visualization techniques using **Python frameworks**.

### Objectives
- Load and explore real-world data  
- Clean and prepare large datasets efficiently  
- Visualize publication patterns and keyword trends  
- Build an interactive web app using Streamlit  

---

## 2️⃣ Data Loading & Cleaning

### Steps Performed
- Loaded a **sample of 2,000 rows** from the original dataset for performance efficiency  
- Cleaned missing values and standardized text columns  
- Converted `publish_time` to `datetime` format  
- Extracted publication `year`  
- Added a new column for abstract word counts  

```python

df["publish_time"] = pd.to_datetime(df["publish_time"], errors="coerce")
df["year"] = df["publish_time"].dt.year
df["abstract_word_count"] = df["abstract"].fillna("").apply(lambda x: len(x.split()))

## 3️⃣ Data Analysis & Visualization

### Key Analyses
- Publications over time – trends in COVID-19 research activity
- Top publishing journals – top 10 journals by publication count
- Word cloud of titles – most frequent words in paper titles
- Abstract length distribution – histogram showing paper length trends

### Libraries Used
- pandas – data cleaning & manipulation
- matplotlib, seaborn – data visualization
- wordcloud – keyword visualization
- streamlit – interactive web interface

### Example Visualization:
*Top 10 Journals Publishing COVID-19 Research (bar chart)*

## 4️⃣ Streamlit Application
*The Streamlit app provides an interactive dashboard to explore the dataset dynamically.*

### App Features
- Filter publications by year range
- View dynamic visualizations (time trends, top journals, word clouds)
- Explore sample data directly in the browser

## Running Locally
*Install dependencies:*
pip install -r requirements.txt
## Run the Streamlit app:
streamlit run meta.py
Or simply explore the hosted version here:
*👉 Live App on Streamlit Cloud* https://nomize-frameworks-assignment-meta-cst38i.streamlit.app/


### 5️⃣ Challenges & Reflections
## Challenges
- Handling a large dataset (>1GB) that couldn’t be easily loaded on limited RAM
- Managing Git and Streamlit Cloud storage constraints
- Optimizing for performance while maintaining analytical depth

## What I Learned
- Practical data cleaning and visualization workflows
- Integrating Python notebooks with Streamlit for web-based analysis
- Efficient handling of real-world data at scale
- Deployment of interactive data apps on cloud platforms

### 6️⃣ Credits
- Dataset: CORD-19 (COVID-19 Open Research Dataset)
- Frameworks: pandas, matplotlib, seaborn, wordcloud, streamlit
- Created by: Nomize

## 🧭 Final Notes
-The app is fully deployed and functional on Streamlit Cloud
- You can clone this repository, replace the sample dataset with your own, and run the analysis locally.
- The analysis output varies depending on the selected publication year range — wider year spans yield richer visualizations.
