import streamlit as st
import pandas as pd
def home():
    st.write("# Chrono-Estimater\n##### This is a simple game inspired by GeoGuessr. Which year do you think this image was taken?")
    x = st.slider('x', min_value = 1900, max_value = 1999)  # time slider
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/5/5d/Berlinermauer.jpg/267px-Berlinermauer.jpg", use_column_width=True)

def hi():
    st.write("Hello there")
page_names_to_funcs = {
    "—": home,
    "Test": hi,
}
ChronoEstimatr2000 = st.sidebar.selectbox("Choose a page", page_names_to_funcs.keys())
page_names_to_funcs[ChronoEstimatr2000]()