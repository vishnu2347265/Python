import streamlit as st
from PIL import Image
st.title('The Title')
st.header('The Header ')
st.subheader('the subheader')


st.markdown("### this a markdown")
st.markdown('''
            - Item1
            - Item2
                1. subitem1
                2. subitem2
            
            ''')

st.code("s1-2024")
st.success("success")