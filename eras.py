import streamlit as st
import math




def twenty():
    confirmed = False
    placeholder = st.empty()
    activeImage = 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5d/Berlinermauer.jpg/267px-Berlinermauer.jpg'
    st.write("# 20th Century")
    st.write("### Choose the year this picture was taken!")
    x = st.number_input(
        "### Choose the year this picture was taken!",
        min_value=1901,
        max_value=2000,
        label_visibility="collapsed",
        step = 1,
        key="button1"
    )  # time slider
    if st.button('Confirm', key='confirmbutton'):
        score1 = round(1000 - (abs((1980-x))*10))
    st.image(activeImage, use_column_width=True)
    st.write("You scored " + str(score1))

    # Second Image
    y = st.number_input(
        "### Choose the year this picture was taken!",
        min_value=1901,
        max_value=2000,
        label_visibility="collapsed",
        step = 1,
        key="button2"
    )  # time slider
    if st.button('Confirm', key='confirmbutton2'):
        score2 = round(1000 - (abs((1963-y))*10))
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/JFK_limousine.png/640px-JFK_limousine.png", use_column_width=True)
    st.write("You scored " + str(score2))

    st.write("Your total score is " + str(score1+score2))

        
        
    


