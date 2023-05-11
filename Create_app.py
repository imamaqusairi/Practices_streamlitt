# -*- coding: utf-8 -*-
"""
Created on Thu May 11 10:41:19 2023

@author: user
"""

import streamlit as st
import numpy as np
import pandas as pd

st.title('Uber Pickups in NYC')

# Fetch Some Data 
DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(10000)
# Notify the reader that the data was successfully loaded.
data_load_state.text('Done ! (using st.cache_data)')


# Inpsect the Raw Data
st.subheader('Raw data')
st.write(data)

st.subheader('Number of pickups by hour')
hist_values = np.histogram(
    data[DATE_COLUMN].dt.hour, bins = 24, range=(0,24))[0]
st.bar_chart(hist_values)


# Plot Data on Map 
st.subheader('Map of all pickups')
st.map(data)


# Plot Data on Map 2
st.subheader('Map of all pickups')
st.map(data)

hour_to_filter = 17
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
st.subheader(f'Map of all pickups at {hour_to_filter}:00')
st.map(filtered_data)

# Filter Results with a slides
hour_to_filter = st.slider('hour', 0, 23, 17)



# Use a button to toggle data
st.subheader('Raw Data')
st.write(data)
if st.checkbox('Show Raw Data'):
    st.subheader('Raw Data')
    st.write(data)
