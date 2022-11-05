import streamlit as st
import pandas as pd
import numpy as np
from eras import twenty
import csv

leaderboard = pd.DataFrame({
    'Player': ["Tetraslam", "Dr Snek", "FireTheLost"],
    'Score': [1000, 500, 100]
})

with st.form(key='playerName'):
    text_input = st.text_input(label='Enter your name')
    submit_button = st.form_submit_button(label='That is indeed my name.')

newplayer = pd.DataFrame({
    'Players': [text_input],
    'Scores': [1000]
})

playerNamesFile = open('playerNames.txt', 'r+')
playerScoresFile = open('playerScores.txt', 'r+')
score = 0

if submit_button:
    playerNamesFile.write("\n"+text_input)
    playerScoresFile.write("\n0")
    addNewPlayer = pd.DataFrame({
        'Playerss': [text_input],
        'Scoress': [0]
    })
    newleaderboard = pd.concat([leaderboard, addNewPlayer], ignore_index=True)
    leaderboard.update(newleaderboard)

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
