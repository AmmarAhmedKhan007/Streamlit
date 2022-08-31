# Libraries

import streamlit as st
import seaborn as sns
import seaborn as sns
import pandas as pd
import plotly.express as px
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Basics Syntaxs

st.title("Khashti App")
st.text("Khashti ke ek App banayan gy is ma")
st.header("Khashti doobh gai")
st.markdown("**Kuxh Be**")

# Title in Top of Screen

st.set_page_config(
    page_title="Real-Time Data Science Dashboard",
    page_icon="✅",
    layout="wide",
)

# Make Containers

header = st.container()
dataset = st.container()
features = st.container()
model_training = st.container()

with header:
    ("Kuxh be")
with dataset:
    ("Kuxh be")
with features:
    ("Kuxh be")
with model_training:
    ("Kuxh be")


# Upload file from PC

with st.sidebar.header(" Upload your Dataset (.csv)"):
    uploaded_file = st.sidebar.file_uploader("Upload your file",type=['csv'])


# Making Columns:
    input, display = st.columns(2)


# Slider:
max_depth= input.slider("How many peoples do you know ?", min_value=10,max_value=100,value=20,step =5)


# n_estimators:
n_estimators= input.selectbox("How many trees should be in NF?",options=[50, 100, 200, 300, 400, 500,'No Limit'])


# Adding list of features
input.write(df.columns)


# Input features from user
input_features= input.text_input("Which features we Use ?")


# Show code in app

if st.checkbox("Show Code"):
    with st.echo():
        #(code)             
        # Paste copy code to Show:


