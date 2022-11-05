import streamlit as st
import pandas as pd

"""
# Hello
"""
x = st.slider('x', min_value = 1900, max_value = 2000)  # time slider
st.write(x, 'squared is', x * x)
st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/5/5d/Berlinermauer.jpg/267px-Berlinermauer.jpg")