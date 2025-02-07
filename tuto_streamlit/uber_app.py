""" Uber pickups APP """
from typing import Optional

import pandas as pd
import plotly.express as px
import streamlit as st

st.title("Uber pickups in NYC")

DATE_COLUMN = "date/time"
DATA_URL = ("https://s3-us-west-2.amazonaws.com/"
            "streamlit-demo-data/uber-raw-data-sep14.csv.gz")


@st.cache_data(persist=True)
def load_data(nrows: Optional[int]) -> pd.DataFrame:
    """ Load dataset

    nrows: Number of rows of file to read. Useful for reading pieces of large files.

    Returns:
         pd.DataFrame: pandas's dataframe with `nrows` rows
    """
    data = pd.read_csv(DATA_URL, nrows=nrows,
                       # parse_dates=["Date/Time"],
                       )
    cols_lowercase = lambda x: str(x).lower()
    data.rename(cols_lowercase, axis="columns", inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data


data_load_state = st.text("Loading data...")
data = load_data(10000)
data_load_state.text("Done! (using st.cache_data)")

if st.checkbox("Show raw data"):
    st.subheader("Raw data")
    st.write(data.head())

st.subheader("Number of pickups by hour")
# st.bar_chart(data[DATE_COLUMN].dt.hour.value_counts(sort=False))
data_delivery = data[DATE_COLUMN].dt.hour.value_counts(sort=False)
fig = px.bar(data_delivery)
st.plotly_chart(fig, theme="streamlit")

# Some number in the range 0-23
default_value = data_delivery.idxmax()  # max pickups time
hour_to_filter = st.slider("hour", min_value=0, max_value=23, value=default_value)  # min: 0h, max: 23h, default: 17h
# filter data based on user's choice
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
# display Map
st.subheader(f"Map of all pickups at {hour_to_filter}:00")
st.map(filtered_data)  # Use the st.map() function to plot the data
