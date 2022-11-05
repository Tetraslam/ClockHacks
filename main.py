import streamlit as st
import pandas as pd
from eras import twenty


def home():
    st.write(
        "# Chrono-Estimater\n##### This is a simple game inspired by GeoGuessr. Which year do you think this image was taken?"
    )
    

page_names_to_funcs = {
    "Home": home,
    "20th Century": twenty,
}

ChronoEstimatr2000 = st.sidebar.selectbox("Choose a page", page_names_to_funcs.keys())
page_names_to_funcs[ChronoEstimatr2000]()
