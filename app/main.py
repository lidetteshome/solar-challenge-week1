# app/main.py

import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from utils import load_data

st.set_page_config(page_title="Solar Insights Dashboard", layout="wide")

st.title("☀️ Cross-Country Solar Data Dashboard ☀️")

# Load data
df = load_data()

# Sidebar filters
countries = st.sidebar.multiselect(
    "Select Countries", options=df["Country"].unique(), default=df["Country"].unique())
metric = st.sidebar.selectbox("Select Metric", ["GHI", "DNI", "DHI"])

# Filtered data
filtered_df = df[df["Country"].isin(countries)]

# Boxplot
st.subheader(f"{metric} Distribution by Country")
fig, ax = plt.subplots(figsize=(8, 5))
sns.boxplot(data=filtered_df, x="Country", y=metric, palette="Set2", ax=ax)
st.pyplot(fig)

# Top irradiance table
st.subheader("🔝 Top 5 Irradiance Records")
top_df = filtered_df.sort_values(by=metric, ascending=False).head(5)
st.dataframe(top_df[["Timestamp", "Country", metric]])
