""" User search dashboard"""

import pandas as pd
import requests
import streamlit as st

st.write("# Welcome to our user search engine! 👋")

first_name = st.sidebar.text_input("What first name are you looking for?")
last_name = st.sidebar.text_input("What last name are you looking for?")
email = st.sidebar.text_input("What email are you looking for?")

response = requests.get(url="http://127.0.0.1:8000/get_data")
data = pd.read_json(response.json())

if st.sidebar.button("Search"):
    first_name_filter = True
    last_name_filter = True
    email_filter = True
    if first_name:
        first_name_filter = data["prénom"].str.contains(first_name, case=False, na=False)
    if last_name:
        last_name_filter = data["nom"].str.contains(last_name, case=False, na=False)
    if email:
        email_filter = data["email"].str.contains(email, case=False, na=False)
    data_result = data.loc[first_name_filter & last_name_filter & email_filter,
                           ["prénom", "nom", "email"]].reset_index(drop=True)
    if data_result.empty:
        st.subheader(f"There are no users corresponding to your parameters \n"
                     f"prenom = {first_name}, nom = {last_name}, email = {email}")
    else:
        st.write(data_result)
