import streamlit as st
from streamlit_dash import StreamlitDash
from app import app

# Set up the Streamlit page
st.set_page_config(page_title="Dash App in Streamlit", layout="wide")

# Create the StreamlitDash integration
st_dash = StreamlitDash(app)

# Run the app
st_dash.run()
