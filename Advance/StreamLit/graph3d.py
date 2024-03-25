from sklearn import datasets
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

data = pd.read_csv('Iris.csv')
st.header('IRIS DATASET')

st.dataframe(data)
st.text(data.info())

st.write(data.describe())

feature = st.selectbox('Select a feature',data.columns)
feature_x = st.selectbox('Select a feature for x axis',data.columns)
feature_y = st.selectbox('Select a feature for y axis',data.columns)
feature_z = st.selectbox('Select a feature for z axis',data.columns)

fig = px.scatter_3d(data, x=feature_x, y=feature_y, z=feature_z, color='Species')
st.plotly_chart(fig)
