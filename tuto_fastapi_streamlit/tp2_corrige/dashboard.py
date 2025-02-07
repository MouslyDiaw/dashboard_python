import streamlit as st

st.set_page_config(
    page_title="Home page",
    page_icon="👋",
    initial_sidebar_state="auto",   # "auto" or "expanded" or "collapsed"
    layout="wide",  # "centered" or "wide"
    menu_items={
        'About': "# This is a header. This is an *extremely* cool app!",
             }
)

st.write("# Welcome to our Marketing Campaign Performance Dashboard! 👋")

st.markdown(
    """ 
    Dear Team,
    We are excited to introduce our new Marketing Campaign Performance Dashboard, 
    designed to offer an insightful overview and in-depth analysis of our ongoing marketing initiatives.
    With our Marketing Campaign Performance Dashboard, we aim to provide a user-friendly and  data-driven 
    approach to assess our marketing efforts, enabling us to make informed decisions and drive greater success.

    We encourage everyone to explore the dashboard to leverage these insights for smarter marketing decisions and
    improved campaign performance.
    """
)
