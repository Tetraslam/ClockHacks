import streamlit as st

from eras import twenty
from eras import calculateScore
from eras import twentyHard

st.set_page_config(
    page_title="Chrono-Estimater | A Game About Time",
    page_icon="🕒",
    layout="wide",
    initial_sidebar_state="expanded",
)


def home():
    st.write("# Chrono-Estimater")
    if "displayScore" not in st.session_state:
        st.write(
            """
            ## Welcome to Chrono-Estimater!

            This is time period based game, inspired by GeoGuessr, that allows players to guess the year different photographs were taken from. Testing your knowledge of history and critical thinking skills, you must piece together clues from each photo, aiming to find the correct year.
            
            ## How to play
            Go to the side bar on the Chrono-Estimator website and choose the desired game mode and time period.
            ## Features
            Different game modes, including Easy and Hard modes.
            - Easy: This tests your recognition of famous historical pictures.
            - Hard: This forces you to use often subtle clues from the picture to figure out from which time period the picture is from.

            
            """
        )
    else:
        st.write(
            "#### You scored "
            + st.session_state["displayScore"]
            + " points last time. Will you beat it this time?"
        )
        st.write(
            """
            ## Welcome to Chrono-Estimater!

            This is time period based game, inspired by GeoGuessr, that allows players to guess the year different photographs were taken from. Testing your knowledge of history and critical thinking skills, you must piece together clues from each photo, aiming to find the correct year.
            ## How to play
            Go to the side bar on the Chrono-Estimator website and choose the desired game mode and time period.
            
            ## Features
            Different game modes, including Easy and Hard modes.
            - Easy: This tests your recognition of famous historical pictures.
            - Hard: This forces you to use often subtle clues from the picture to figure out from which time period the picture is from.

            
            """
        )


page_names_to_funcs = {
    "Home": home,
    "20th Century (Easy Mode)": twenty,
    "20th Century (Hard Mode)": twentyHard
}

ChronoEstimatr2000 = st.sidebar.selectbox("Choose a page", page_names_to_funcs.keys())
page_names_to_funcs[ChronoEstimatr2000]()
