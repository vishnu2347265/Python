# Importing necessary libraries

import streamlit as st
import pandas as pd
import plost

st.set_page_config(layout='wide', initial_sidebar_state='expanded')

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Read the CSV file
df = pd.read_csv('shopping_behavior_updated.csv')



# Key Metrics
total_sales = df['Purchase Amount (USD)'].sum()
average_purchase_amount = df['Purchase Amount (USD)'].mean()
customer_demographics = df[['Age', 'Gender']].describe()





    
# Adding sidebar contents

st.sidebar.header('Dashboard')

# Main Content
st.title('Consumer Behavior Analysis Dashboard')


st.sidebar.subheader('Heat map parameter')
time_hist_color = st.sidebar.selectbox('Color by', ('temp_min', 'temp_max')) 

st.sidebar.subheader('Donut chart parameter')
donut_theta = st.sidebar.selectbox('Select data', ('q2', 'q3'))

st.sidebar.subheader('Line chart parameters')
plot_data = st.sidebar.multiselect('Select data', ['temp_min', 'temp_max'], ['temp_min', 'temp_max'])
plot_height = st.sidebar.slider('Specify plot height', 200, 500, 250)


# Key Metrics Section
st.subheader('Key Metrics')
st.write(f"Total Sales: ${total_sales:.2f}")
st.write(f"Average Purchase Amount: ${average_purchase_amount:.2f}")
st.write('Customer Demographics:')
st.write(customer_demographics)


# Adding dashboard contents

# Row A
st.markdown('### Metrics')
col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "20 °C", "2 °C")
col2.metric("Wind", "11 kmph", "-8%")
col3.metric("Humidity", "86%", "4%")


# Row B
seattle_weather = pd.read_csv('https://raw.githubusercontent.com/tvst/plost/master/data/seattle-weather.csv', parse_dates=['date'])
stocks = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/stocks_toy.csv')

c1, c2 = st.columns((7,3))
with c1:
    st.markdown('### Heatmap')
    plost.time_hist(
    data=seattle_weather,
    date='date',
    x_unit='week',
    y_unit='day',
    color=time_hist_color,
    aggregate='median',
    legend=None,
    height=345,
    use_container_width=True)
with c2:
    st.markdown('### Donut chart')
    plost.donut_chart(
        data=stocks,
        theta=donut_theta,
        color='company',
        legend='bottom', 
        use_container_width=True)

# Row C
st.markdown('### Line chart')
st.line_chart(seattle_weather, x = 'date', y = plot_data, height = plot_height)
