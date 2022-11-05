import streamlit as st
import pandas as pd

"""
# Hello
"""
x = st.slider('x', min_value = 1900, max_value = 2000)  # 👈 this is a widget
st.write(x, 'squared is', x * x)