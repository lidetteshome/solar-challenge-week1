# app/utils.py

import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    benin = pd.read_csv("../data/benin_clean.csv")
    sierra = pd.read_csv("../data/sierraleone_clean.csv")
    togo = pd.read_csv("../data/togo_clean.csv")
    
    benin["Country"] = "Benin"
    sierra["Country"] = "Sierra"
    togo["Country"] = "Togo"
    
    return pd.concat([benin, sierra, togo], ignore_index=True)