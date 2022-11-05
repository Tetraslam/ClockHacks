import streamlit as st
import pandas as pd
from eras import twentiethcentury as twenty

page_names_to_funcs = {
    "Home": home,
    "20th Century": twenty,
}


def home():
    st.write(
        "# Chrono-Estimater\n##### This is a simple game inspired by GeoGuessr. Which year do you think this image was taken?"
    )
    st.write("### Choose the year this picture was taken!")
    x = st.slider(
        "### Choose the year this picture was taken!",
        min_value=1901,
        max_value=2000,
        label_visibility="collapsed",
    )  # time slider
    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5d/Berlinermauer.jpg/267px-Berlinermauer.jpg",
        use_column_width=True,
    )


ChronoEstimatr2000 = st.sidebar.selectbox("Choose a page", page_names_to_funcs.keys())
page_names_to_funcs[ChronoEstimatr2000]()
