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
├── notebooks <br>
│   └── README.md <br>
├── requirements.txt <br>
├── scripts <br>
│   └── README.md <br>
├── src <br>
└── tests <br>

