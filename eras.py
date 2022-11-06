import streamlit as st
import math




def twenty():
    index = 1
    score = 0
    confirmed = False
    placeholder = st.empty()
    activeImage = 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5d/Berlinermauer.jpg/267px-Berlinermauer.jpg'
    st.write("# 20th Century")
    st.write("### Choose the year this picture was taken!")
    x = st.slider(
        "### Choose the year this picture was taken!",
        min_value=1901,
        max_value=2000,
        label_visibility="collapsed",
    )  # time slider
    finalx = 0
    if st.button('Confirm', key='confirmbutton'):
        year = 1980
        score = (1000 / 3) * math.log((1000 / (1 + abs(year - x))), 10)
        index+=1
    st.image(activeImage, use_column_width=True)
    
    
    st.write("You scored " + str(score))
        
        
    


