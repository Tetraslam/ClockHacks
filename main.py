import streamlit as st
import pandas as pd

"""
# Hello
"""
x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)