"""Streamlit dashboard"""
from typing import Optional

import pendulum
import streamlit as st
import requests
import pandas as pd

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Campaign overview",
                   layout="wide",
                   initial_sidebar_state="auto",
                   page_icon="🎨",
                   )


@st.cache_data()
def get_data():
    response = requests.get(f"{API_URL}/get_data")
    return pd.read_json(response.json(),
                        dtype={"cookie_id": str,
                               "campaign_id": str,
                               "external_site_id": str,
                               "product_id": str,
                               },
                        convert_dates=["date_impression", "date_clic", "date_achat"])


data = get_data()

st.sidebar.subheader('Filters :')

campaign_id = st.sidebar.selectbox("Which campaign do you need data for?",
                                   data.campaign_id.unique(),
                                   index=None,
                                   placeholder="Choose a campaign",
                                   )
click_date = st.sidebar.date_input(
    "Do you only want to see campaigns that get a click at/before?",
    # (pendulum.now().subtract(years=3), pendulum.now()),
    min_value=pendulum.now().subtract(years=10),
    max_value=pendulum.now(),
    format="YYYY-MM-DD",
    value=None,
)
click_action = st.sidebar.checkbox("Do you want to display only campaigns that get a click?", key='click_action')

achat_action = st.sidebar.checkbox("Achat action", key='achat_action')

if st.sidebar.button("Get campaign data"):
    data_campaign = data.copy()
    if campaign_id:
        data_campaign = data_campaign.loc[data.campaign_id == campaign_id]
    if click_action:
        data_campaign = data_campaign.loc[data_campaign.is_clic]
    if click_date:
        data_campaign = data_campaign.loc[data_campaign.date_clic.dt.date <= click_date]
    st.write(data_campaign.head())
    st.subheader("Data summarize")
    st.write(data_campaign.describe(include="all"))
    nb_data = len(data_campaign)
else:
    st.subheader("Data overview")
    st.write(data.head())
    st.subheader("Data summarize")
    st.write(data.describe(include="all"))
    nb_data = len(data)
