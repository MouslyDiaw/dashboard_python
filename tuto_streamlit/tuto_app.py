"""Tuto sur Streamlit."""
import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

st.title("Tutoriel sur Streamlit")

st.subheader("Discovery streamlit widgets..")
st.write("Here's our first attempt at using data to create a table:")

# create a fake dataset
df = pd.DataFrame({'first column': [1, 2, 3, 4],
                   'second column': [10, 20, 30, 40]})
st.write("Display dataframe with st.write...")
st.write(df)  # drawing a dataframe as an interactive table
st.write("Display dataframe with st.dataframe...")
st.dataframe(df)
st.write("Display dataframe with st.table...")
st.table(df)  # draw a dataframe as a static table

x = st.slider('x')  # 👈 this is a widget
st.write(f"{x} squared is {x*x}")

prenom = st.text_input("Your name", key="name")  # You can access the value at any point with:
st.write(f"My name is: {prenom}")
# st.session_state.name


# ---------------- Drawing
st.subheader("----------------- Drawing -----------------")

chart_data = df
clicked_update = st.checkbox('Update dataframe')
clicked_draw = st.checkbox('Draw line')
if clicked_update:
    chart_data = pd.DataFrame(
         np.random.randn(20, 3),
         columns=['a', 'b', 'c'])
    st.write(chart_data)

if clicked_draw:
    clicked_update = False
    st.line_chart(chart_data)


# selectbox
df = pd.DataFrame({'first column': [1, 2, 3, 4],
                   'second column': [10, 20, 30, 40]}
                  )

option = st.selectbox('Which number do you like best?',
                      df['first column'])
st.write(f"You selected: {option}")

# Créer un graphique Plotly
fig = px.line(chart_data)
# Afficher le graphique dans Streamlit
st.plotly_chart(fig)

# Map
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)
