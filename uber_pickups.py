
import streamlit as st
import pandas as pd
import numpy as np

st.title("Uber Pickups in New York City")

DATA_URL = (
    "https://raw.githubusercontent.com/streamlit/"
    "demo-uber-nyc-pickups/main/uber-raw-data-sep14.csv.gz"
)

@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    data.columns = data.columns.str.lower()
    data["date/time"] = pd.to_datetime(data["date/time"])
    return data

data = load_data(10000)

if st.checkbox("Show raw data"):
    st.subheader("Raw data")
    st.write(data)

st.subheader("Number of pickups by hour")
hist_values = np.histogram(
    data["date/time"].dt.hour,
    bins=24,
    range=(0, 24)
)[0]
st.bar_chart(hist_values)

hour_to_filter = st.slider("Hour", 0, 23, 17)

filtered_data = data[
    data["date/time"].dt.hour == hour_to_filter
]

st.subheader(f"Map of all pickups at {hour_to_filter}:00")
st.map(filtered_data)
