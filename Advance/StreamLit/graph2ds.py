from sklearn import datasets
import streamlit as st
import pandas as pd
import numpy as n
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('Iris.csv')
st.header('IRIS DATASET')

st.dataframe(data)
st.text(data.info())

st.write(data.describe())

feature = st.selectbox('Select a feature',data.columns)
feature_x = st.selectbox('Select a feature for x axis',data.columns)
feature_y = st.selectbox('Select a feature for y axis',data.columns)
fig,ax = plt.subplots()
# sns.barplot(x=feature_x, y=feature_y, hue=data.Species, data=data)
# st.pyplot(fig)

sns.scatterplot(data=data, x=feature_x,y=feature_y,hue=data.Species,ax=ax)
plt.title('Scatter plot of Sepal Length for Iris Species with Target')  
st.pyplot(fig)


# #histo
# fig,ax = plt.subplots()
# ax.hist(data[feature],bins=30,edgecolor='black')

