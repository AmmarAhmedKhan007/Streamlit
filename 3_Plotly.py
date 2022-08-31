import streamlit as st
import plotly.express as px
import pandas as pd

st.title('Plotly Graph')

# Import Dataset
df = px.data.gapminder()
st.write(df)
st.write(df.columns)

# Summary
st.write(df.describe())

# Manage Data
year_option = df['year'].unique().tolist()
year = st.selectbox("Which Year we should Plot ?",year_option, 0)
# df = df[df['year']==year]                        # Animation year Base

# Plotting
fig = px.scatter(df, x='gdpPercap', y='lifeExp', size ='pop' ,color='country', hover_name='country',log_x=True, 
                size_max=55, range_x=[100, 100000], range_y=[20, 90],
                animation_frame='year' ,animation_group='country')      # for animation
st.write(fig)