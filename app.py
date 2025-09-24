import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# App title and description
st.title("CORD-19 Data Explorer")
st.write("Simple exploration of COVID-19 research papers (sample of ~10,000 papers). Analyze publications by year, top journals, title words, and sources.")

# Load cleaned data
@st.cache_data
def load_data():
    return pd.read_csv('cleaned_metadata.csv', low_memory=False)

df = load_data()

# Interactive widgets
st.header("Filter Data")
year_range = st.slider("Select year range", int(df['year'].min()), int(df['year'].max()), (2020, 2021))
journal_options = ['All'] + list(df['journal'].unique())
selected_journal = st.selectbox("Select journal", journal_options)

# Filter data based on widgets
filtered_df = df[(df['year'].between(year_range[0], year_range[1]))]
if selected_journal != 'All':
    filtered_df = filtered_df[filtered_df['journal'] == selected_journal]

# Display sample data
st.header("Sample Data")
st.write(f"Showing {len(filtered_df)} papers after filtering")
st.dataframe(filtered_df[['title', 'year', 'journal', 'abstract_word_count']].head())

# Display visualizations
st.header("Visualizations")
st.subheader("Publications by Year")
st.image('plots/publications_by_year.png')

st.subheader("Top 10 Journals")
st.image('plots/top_journals.png')

st.subheader("Word Cloud of Paper Titles")
st.image('plots/title_wordcloud.png')

st.subheader("Distribution of Papers by Source")
st.image('plots/source_distribution.png')

# Footer
st.write("Built by Oluwaseun for Power Learn Project Capstone. Data: CORD-19 dataset.")