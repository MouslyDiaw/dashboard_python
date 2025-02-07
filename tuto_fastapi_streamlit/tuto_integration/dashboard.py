""" Streamlit Dashbaord."""
import json
import requests
import streamlit as st

st.title("Basic calculator App")

# take user'inputs
operation = st.selectbox("What operation you want to perform?",
                         ("Addition", "Subtraction", "Multiplication", "Division"),
                         index=None,
                         placeholder="Choose an option")

st.write("Select the numbers from slider below")
x = st.slider("X", min_value=0, max_value=1000, step=20)
y = st.slider("Y", min_value=0, max_value=1000, step=10)

# convert the inputs into json format
user_inputs = {"operation": operation, "x": x, "y": y}

# when the user clicks on button it will fetch he API
if st.button("Calculate"):
    response = requests.post(url="http://127.0.0.1:8000/calculate", data=json.dumps(user_inputs))
    status_code = response.status_code
    if status_code == 200:
        # data = response.json()
        st.subheader(f"Response from API = {response.text}")
    else:
        st.write(f"Execution error: {status_code}")
