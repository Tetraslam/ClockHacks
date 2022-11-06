import streamlit as st
import pandas as pd
import numpy as np
from eras import twenty
import csv
import eras


def firstrun():
    if 'runbefore' not in st.session_state:
        st.session_state['runbefore'] = 'run'
        return(st.session_state['runbefore'])

if firstrun() == 'run':
    st.write('hello')




leaderboard = pd.DataFrame({
    'Player': ["Tetraslam", "Dr Snek", "FireTheLost"],
    'Score': [1000, 500, 100]
})

#with st.form(key='playerName'):
#    text_input = st.text_input(label='Enter your name')
#    submit_button = st.form_submit_button(label='That is indeed my name.')

def home():
    st.write(
        "# Chrono-Estimater\n##### This is a game inspired by GeoGuessr. Guess the years that pictures were taken in!"
    )
    st.write(leaderboard)
    
    

page_names_to_funcs = {
    "Home": home,
    "20th Century": twenty,
}

ChronoEstimatr2000 = st.sidebar.selectbox("Choose a page", page_names_to_funcs.keys())
page_names_to_funcs[ChronoEstimatr2000]()
