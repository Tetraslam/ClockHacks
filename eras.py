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
        key=1
    )  # time slider
    if st.button('Confirm', key='confirmbutton'):
        year = 1980
        score = round(1000 - (abs((year-x))*10))
        index+=1
    st.image(activeImage, use_column_width=True)
    st.write("You scored " + str(score))

    # Second Image
    y = st.slider(
        "### Choose the year this picture was taken!",
        min_value=1901,
        max_value=2000,
        label_visibility="collapsed",
        key=2
    )  # time slider
    if st.button('Confirm', key='confirmbutton2'):
        year = 1963
        score = round(1000 - (abs((year-y))*10))
        index+=1
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/JFK_limousine.png/640px-JFK_limousine.png", use_column_width=True)
    st.write("You scored " + str(score))


        
        
    


