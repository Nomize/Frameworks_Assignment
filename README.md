# Python Frameworks Assignment: CORD-19 Data Analysis and Streamlit App

Welcome to my **Python Frameworks Assignment**! This repository contains my work analyzing the [CORD-19](https://www.semanticscholar.org/cord19) dataset, performing data cleaning, visualization, and building an interactive Streamlit app.

---

## 📂 Repository Structure

Frameworks_Assignments/
├── meta.py # Streamlit app code
├── pyDA.ipynb # Jupyter Notebook for data exploration & visualization
├── .gitignore # Ignores metadata.csv
└── README.md # Project documentation

> **Note:** The `metadata.csv` dataset is **not included** in the repo due to its large size (>1GB). Please download it separately from the [CORD-19 dataset] (https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge) if you wish to run the analysis locally.

---

## 📝 Assignment Overview

This project explores the CORD-19 research dataset (COVID-19 papers) and demonstrates:

- Loading and exploring real-world datasets
- Data cleaning and preparation
- Basic data analysis and visualizations
- Building an interactive Streamlit application

---



---

## 1️⃣ Data Loading and Exploration

**Steps performed:**

- Loaded a sample of 100,000 rows from `metadata.csv` using `pandas`.
- Examined the first few rows to understand the data structure.
- Explored dataset dimensions, data types, and missing values.
- Generated basic statistics for numerical columns.

**Key Columns Used:**

| Column Name     | Description                                |
|-----------------|--------------------------------------------|
| `title`         | Title of the research paper                |
| `abstract`      | Paper abstract                             |
| `publish_time`  | Publication date                           |
| `journal`       | Publishing journal                         |
| `authors`       | List of authors                            |

---

## 2️⃣ Data Cleaning and Preparation

**Actions Taken:**

- Handled missing values by filling abstracts with empty strings.
- Converted `publish_time` to datetime format.
- Extracted `year` from publication date for analysis.
- Added new column `abstract_word_count` to analyze abstract lengths.

```python
df["publish_time"] = pd.to_datetime(df["publish_time"], errors="coerce")
df["year"] = df["publish_time"].dt.year
df["abstract_word_count"] = df["abstract"].fillna("").apply(lambda x: len(x.split()))


3️⃣ Data Analysis and Visualization

Analyses Performed:

Number of publications over time – visualized yearly publication counts.

Top journals publishing COVID-19 research – bar chart of top 10 journals.

Most frequent words in paper titles – generated a word cloud.

Abstract word count distribution – histogram of abstract lengths.

Technologies Used:

pandas for data manipulation

matplotlib & seaborn for visualizations

WordCloud for generating word clouds

Sample Visualization:

Top 10 Journals Bar Chart


You can run the notebook locally to generate all plots dynamically.

4️⃣ Streamlit Application

Features:

Interactive slider to filter papers by publication year.

Displays a sample of filtered data.

Shows dynamic visualizations:

Publications over time

Top journals

Word cloud of paper titles

Abstract word count distribution

Running the App:

Make sure Streamlit is installed:

pip install streamlit


Run the app from your terminal/command prompt:

streamlit run meta.py

5️⃣ Challenges and Reflection

Challenges:

The dataset is very large (>1GB), which made loading it a challenge.

Filtering and processing large datasets required memory-efficient techniques.

Learning to integrate Jupyter analysis with Streamlit visualization.

What I Learned:

Practical experience in data cleaning, analysis, and visualization.

How to create an interactive web app using Streamlit.

Understanding the workflow of a real-world data science project from raw data to insights.

6️⃣ Credits

CORD-19 Dataset
 – COVID-19 Open Research Dataset

Python Libraries: pandas, matplotlib, seaborn, wordcloud, streamlit

