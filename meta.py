import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# --- Load Data ---
cols = ["title", "abstract", "publish_time", "journal", "authors"]
df = pd.read_csv("metadata.csv", usecols=cols, nrows=100000, low_memory=False)

# --- Preprocess Data ---
df["publish_time"] = pd.to_datetime(df["publish_time"], errors="coerce")
df["year"] = df["publish_time"].dt.year
df["abstract_word_count"] = df["abstract"].fillna("").apply(lambda x: len(str(x).split()))
df["abstract_word_count"] = pd.to_numeric(df["abstract_word_count"], errors="coerce")

# --- Streamlit App Layout ---
st.title("CORD-19 Data Explorer")
st.write("Explore COVID-19 research papers interactively with filters and visualizations.")

# Sidebar for interactive filters
st.sidebar.header("Filters")
year_range = st.sidebar.slider(
    "Select Year Range",
    int(df["year"].min()),
    int(df["year"].max()),
    (2020, 2021)
)
top_n = st.sidebar.slider(
    "Number of Top Journals to Display",
    min_value=5,
    max_value=30,
    value=10
)

# Filter data by selected year
filtered_df = df[(df["year"] >= year_range[0]) & (df["year"] <= year_range[1])]

# Show sample data
st.subheader("Sample of Data")
st.dataframe(filtered_df.head(10))

# --- Visualization 1: Publications Over Time ---
st.subheader("Publications Over Time")
pubs_by_year = filtered_df["year"].value_counts().sort_index()
fig, ax = plt.subplots()
sns.barplot(x=pubs_by_year.index, y=pubs_by_year.values, ax=ax, palette="Blues_r")
ax.set_xlabel("Year")
ax.set_ylabel("Number of Papers")
ax.set_title("Publications by Year")
st.pyplot(fig)

# --- Visualization 2: Top Journals ---
st.subheader(f"Top {top_n} Journals Publishing COVID-19 Research")
top_journals = filtered_df["journal"].value_counts().head(top_n)
fig, ax = plt.subplots()
sns.barplot(y=top_journals.index, x=top_journals.values, ax=ax, palette="Greens_r")
ax.set_xlabel("Number of Papers")
ax.set_ylabel("Journal")
ax.set_title(f"Top {top_n} Journals")
st.pyplot(fig)

# --- Visualization 3: Stylish Word Cloud ---
st.subheader("Word Cloud of Paper Titles")
titles = " ".join(filtered_df["title"].dropna())
wordcloud = WordCloud(
    width=800,
    height=400,
    background_color="black",
    colormap="plasma",
    contour_color='white',
    contour_width=3,
    max_words=200,
    min_font_size=10,
    prefer_horizontal=0.9
).generate(titles)
fig, ax = plt.subplots(figsize=(12, 6))
ax.imshow(wordcloud, interpolation="bilinear")
ax.axis("off")
st.pyplot(fig)

# --- Visualization 4: Abstract Word Count Distribution ---
# Ensure abstract_word_count is numeric and drop NaNs
word_counts = pd.to_numeric(filtered_df["abstract_word_count"], errors="coerce").dropna()

# Plot histogram
fig, ax = plt.subplots()
sns.histplot(word_counts, bins=50, kde=False, color="purple", ax=ax)
ax.set_xlabel("Word Count")
ax.set_ylabel("Frequency")
ax.set_title("Distribution of Abstract Word Counts")
st.pyplot(fig)

