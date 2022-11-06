import streamlit as st
import pandas as pd
import numpy as np
from eras import twenty
import csv
import eras
from eras import calculateScore

st.set_page_config(
   page_title="Chrono-Estimater | Home",
   page_icon="🕒",
   layout="wide",
   initial_sidebar_state="expanded",
)
#with st.form(key='playerName'):
#    text_input = st.text_input(label='Enter your name')
#    submit_button = st.form_submit_button(label='That is indeed my name.')

def home():
    st.write(
        "# Chrono-Estimater\n##### This is a game inspired by GeoGuessr. Guess the years that pictures were taken in!"
    )
    if 'displayScore' not in st.session_state:
        st.write("Welcome to Chrono-Estimater!")
    else:
        st.write("You scored " + st.session_state['displayScore'] + " points last time. Will you beat it this time?")

    
    

page_names_to_funcs = {
    "Home": home,
    "20th Century": twenty,
}

ChronoEstimatr2000 = st.sidebar.selectbox("Choose a page", page_names_to_funcs.keys())
page_names_to_funcs[ChronoEstimatr2000]()
