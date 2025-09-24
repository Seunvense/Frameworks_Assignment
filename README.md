CORD-19 Data Explorer
Overview
This project is a Power Learn Project Capstone Assignment analyzing the CORD-19 dataset (sample of ~10,000 papers) to explore COVID-19 research papers. It includes data loading, cleaning, analysis, visualizations, and a Streamlit app for interactive exploration.
Files

analysis.ipynb: Jupyter Notebook with data loading, cleaning, analysis, and visualizations.
app.py: Streamlit app displaying filtered data and visualizations.
sample_metadata.csv: Sample dataset (10,000 rows, ~10 MB).
cleaned_metadata.csv: Cleaned dataset (~8 MB).
plots/: Visualizations (PNG files: publications by year, top journals, title word cloud, source distribution).
.gitignore: Excludes large files and caches.

Part 1: Data Loading and Exploration

Loaded sample_metadata.csv (~10,000 rows).
Checked shape (~10,000 rows, 15 columns), data types (mostly strings), missing values (abstract: ~20-30% nulls), and basic statistics.

Part 2: Data Cleaning and Preparation

Dropped rows missing title or publish_time.
Filled missing abstract, journal, authors with defaults.
Converted publish_time to datetime, extracted year, added abstract_word_count.
Saved to cleaned_metadata.csv (~9,900 rows).

Part 3: Data Analysis and Visualization

Analyzed papers by year (peak in 2020), top journals (e.g., The Lancet), title word frequencies (e.g., "COVID-19"), and source distribution (e.g., PMC).
Visualizations:
Bar chart: Publications by year (plots/publications_by_year.png).
Bar chart: Top 10 journals (plots/top_journals.png).
Word cloud: Paper titles (plots/title_wordcloud.png).
Bar chart: Source distribution (plots/source_distribution.png).

Part 4: Streamlit Application

Built app.py with:
Title and description.
Slider for year range, dropdown for journals.
Filtered data table (title, year, journal, word count).
All 4 visualizations from Part 3.

Run locally: streamlit run app.py.

Part 5: Documentation and Reflection
Findings

Most papers published in 2020, reflecting the COVID-19 research surge.
Top journals include The Lancet, Nature, and PLoS One.
Frequent title words: "COVID-19", "SARS-CoV-2", "coronavirus".
Sources like PMC and WHO dominate the dataset.

Challenges

Large dataset (257 MB) caused memory errors; used sample (10 MB) for efficiency.
Learning Streamlit widget syntax was tricky but rewarding.
Handling missing data required careful decisions (e.g., filling abstracts).

Learning

Gained skills in pandas for data cleaning and analysis.
Mastered visualization with matplotlib, seaborn, and wordcloud.
Learned to build interactive apps with Streamlit.
Improved Git workflow and Jupyter notebook organization.

Usage

Install dependencies: pip install pandas matplotlib seaborn streamlit wordcloud.
Run analysis: Open analysis.ipynb in Jupyter.
Run app: streamlit run app.py.
View repo: https://github.com/Seunvense/Frameworks_Assignment.

Submission
GitHub repo: https://github.com/Seunvense/Frameworks_Assignment
Built by Oluwaseun for Power Learn Project, September 2025. Data: CORD-19 dataset.
