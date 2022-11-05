import streamlit as st
import pandas as pd

"""
# Hello
"""

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

df
import numpy as np
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])
     st.write("Hello there")

st.line_chart(chart_data)