# Solar Energy Data Challenge – Week 0

Welcome to the Week 0 project for the 10Academy AI for Fintech program!  
This repository documents my work on solar irradiance data across three African countries — **Benin**, **Sierra Leone**, and **Togo** — with the aim of supporting strategic solar energy investments.

---

## Task Overview

This week’s focus was on setting up the project pipeline and performing robust data cleaning + exploratory data analysis (EDA).  
The work was divided into the following steps.

### ✅ Task 1: Git & Project Setup
- Created a structured project repository using Git & GitHub
- Added `.gitignore`, `requirements.txt`, and GitHub Actions CI (`ci.yml`)
- Set up environment and CI/CD script for reproducibility

### ☑️ Task 2: Data Cleaning & EDA
Started performing in-depth analysis on irradiance and environmental data from the following countries.
- 🇧🇯 Benin (Malanville)
- 🇸🇱 Sierra Leone (Bumbuna)
- 🇹🇬 Togo (Dapaong)

#### Planned Main cleaning steps:
- Remove **negative irradiance values** (GHI, DNI, DHI) which are non-physical
- Detect and remove **outliers** using Z-score filtering ($|Z| > 3$)
- Drop irrelevant columns (e.g., `Comments`)

#### EDA highlights:
- Visualize daily average irradiance & temperature trends
- Analyze impact of panel cleaning on ModA & ModB
- Correlation heatmaps for all environmental variables
- Scatter and bubble plots for GHI vs wind speed, humidity, and temperature

---

## 📁 Project Structure

solar-challenge-week1 <br>
├── LICENSE <br>
├── README.md <br>
├── app <br>
│   ├── __init__.py <br>
│   ├── __pycache__ <br>
│   │   └── utils.cpython-312.pyc <br>
│   ├── main.py <br>
│   └── utils.py <br>
├── data <br>
│   ├── benin-malanville.csv <br>
│   ├── benin_clean.csv <br>
│   ├── sierraleone-bumbuna.csv <br>
│   ├── sierraleone_clean.csv <br>
│   ├── togo-dapaong_qc.csv <br>
│   └── togo_clean.csv <br>
├── figures <br>
│   ├── average_ghi_by_country.png <br>
│   ├── benin_bubble_ghi_tamb.png <br>
│   ├── benin_cleaning_impact.png <br>
│   ├── benin_correlation_heatmap.png <br>
│   ├── benin_ghi_histogram.png <br>
│   ├── benin_rh_vs_tamb.png <br>
│   ├── benin_timeseries.png <br>
│   ├── benin_ws_histogram.png <br>
│   ├── benin_ws_vs_ghi.png <br>
│   ├── compare_dhi_boxplot.png <br>
│   ├── compare_dni_boxplot.png <br>
│   ├── compare_ghi_boxplot.png <br>
│   ├── sierraleone_bubble_ghi_tamb.png <br>
│   ├── sierraleone_cleaning_impact.png <br>
│   ├── sierraleone_correlation_heatmap.png <br>
│   ├── sierraleone_ghi_histogram.png <br>
│   ├── sierraleone_rh_vs_tamb.png <br>
│   ├── sierraleone_timeseries.png <br>
│   ├── sierraleone_ws_histogram.png <br>
│   ├── sierraleone_ws_vs_ghi.png <br>
│   ├── togo_bubble_ghi_tamb.png <br>
│   ├── togo_cleaning_impact.png <br>
│   ├── togo_correlation_heatmap.png <br>
│   ├── togo_ghi_histogram.png <br>
│   ├── togo_rh_vs_tamb.png <br>
│   ├── togo_timeseries.png <br>
│   ├── togo_ws_histogram.png <br>
│   └── togo_ws_vs_ghi.png <br>
├── notebooks <br>
│   ├── README.md <br>
│   ├── benin_eda.ipynb <br>
│   ├── compare_countries.ipynb <br>
│   ├── sierraleone_eda.ipynb <br>
│   └── togo_eda.ipynb <br>
├── requirements.txt <br>
├── scripts <br>
│   ├── README.md <br>
│   └── __init__.py <br>
├── src <br>
└── tests <br>
