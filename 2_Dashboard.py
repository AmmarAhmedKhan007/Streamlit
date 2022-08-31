import streamlit as st
import seaborn as sns
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Make Containers

header = st.container()
dataset = st.container()
features = st.container()
model_training = st.container()

with header:
    st.title("Khashti App")
    st.text("Khashti ke ek App banayan gy is ma")


with dataset:
    st.header("Khashti doobh gai")
    st.text("we work on Titanic Dataset ")
    df = sns.load_dataset("titanic")
    df = df.dropna()
    st.write(df.head())

    st.subheader("Sex chart")
    st.bar_chart(df['sex'].value_counts())

    st.subheader("Alive chart")
    st.bar_chart(df['alive'].value_counts())

    st.subheader("Class ka Hisaab sa")
    st.bar_chart(df['class'].value_counts())

    st.subheader("Kitny dooby kitny Bachayy")
    st.bar_chart(df['survived'].value_counts())

with features:
    st.header("These are our features")
    st.text("bhot saray features ka sath")
    st.markdown(" 1. **Feature 1:** This will tell us KuxH Be.")
    st.markdown(" 2. **Feature 2:** This will tell us KuxH Be.")
    st.markdown(" 3. **Feature 3:** This will tell us KuxH Be.")


with model_training:
    st.header("Train Khashti model")
    st.text("Kia bna khashti walon ka")

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

# Machine Learning Model
model = RandomForestRegressor(max_depth=max_depth, n_estimators=n_estimators)

# Adding Condition To resolve ( No Limit) prolem
if n_estimators == 'No Limit':
    model = RandomForestRegressor(max_depth=max_depth)
else:
    model = RandomForestRegressor(max_depth=max_depth, n_estimators=n_estimators)

# Define X and Y

X = df[[input_features]]
Y = df[['fare']]

# Fit model

model.fit(X, Y)
pred = model.predict(Y)

# Display metrices

display.subheader("Mean Absolute Value of Model is : ")
display.write(mean_absolute_error(Y, pred))

display.subheader("Mean Squared Error of Model is : ")
display.write(mean_squared_error(Y, pred))

display.subheader("R Squared Score of Model is : ")
display.write(r2_score(Y, pred))