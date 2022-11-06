import streamlit as st
import math


def calculateScore(input, year):
    return round(10000 / (abs((year-input+1))))


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
        st.write("You scored " + str(calculateScore(x, 1980)))
        if calculateScore(x, 1980) == 1000:
            st.write("That's correct! Good job.")
        else:
            st.write("The correct year was 1980")
    st.image(activeImage, use_column_width=True)
    

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
        st.write("You score " +str(calculateScore(y, 1963)))
        if calculateScore(y, 1963) == 1000:
            st.write("That's correct! Well done.")
        else:
            st.write("The correct year was 1963.")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/JFK_limousine.png/640px-JFK_limousine.png", use_column_width=True)

    # Third Image
    z = st.number_input(
        "### Choose the year this picture was taken!",
        min_value=1901,
        max_value=2000,
        label_visibility="collapsed",
        step = 1,
        key="button3"
    )  # time slider
    if st.button('Confirm', key='confirmbutton3'):
        st.write("You score " +str(calculateScore(z, 1951)))
        if calculateScore(z, 1951) == 1000:
            st.write("That's correct! Well done.")
        else:
            st.write("The correct year was 1951.")
    st.image("https://upload.wikimedia.org/wikipedia/en/8/86/Einstein_tongue.jpg", use_column_width=True)


    st.write("## Your total score is " + str(calculateScore(x, 1980) + calculateScore(y, 1963) + calculateScore(z, 1951)))
    st.session_state['displayScore'] = str(calculateScore(x, 1980) + calculateScore(y, 1963) + calculateScore(z, 1951))



    


