import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

st.set_page_config(                                 
    page_title="Exploratory Data Analysis",            
    page_icon="✅",
    layout="wide",
)                                 

# Title

st.markdown('''
# **Exploratory Data Analysis Web App**
This app is Daeveloped By **Ammar Ahmed** called
**EDA App**
''')

# Upload file from PC

with st.sidebar.header(" Upload your Dataset (.csv)"):
    uploaded_file = st.sidebar.file_uploader("Upload your file",type=['csv'])
    
    df = sns.load_dataset("iris")
    st.sidebar.markdown("[Example csv file]")

# Profiling reports for Pandas

if uploaded_file is not None:
    @st.cache
    def load_csv():
        csv =pd.read_csv(uploaded_file) 
        return csv
    df = load_csv()
    pr = ProfileReport (df, explorative=True)
    st.header("**Input DataFrame**")
    st.write(df)
    st.write("---")
    st.header("**Profiling Report with Pandas**")
    st_profile_report(pr)
else:
    st.info("Awaiting for CSV file")
    if st.button("Press to use Example data"):
    # Example Data
        @st.cache
        def load_data():
            a= pd.DataFrame(np.random.rand(100, 5),
            columns=['Age','Name','Example','KuxhBe','KuxhNi'])
            return a
        df = load_data()
        pr = ProfileReport (df, explorative=True)
        st.header("**Input DataFrame")
        st.write(df)
        st.write("---")
        st.header("**Profiling Report with Pandas**")
        st_profile_report(pr)