import streamlit as st
import math


def calculateScore(input, year):
    return round((10000/math.log(2, 10))*math.log(1 + input/year))

def calculateScoreHard(input, year):
    return round(10*(1000 / 3) * math.log((1000 / (1 + abs(year - input))), 10))


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
        st.write("You score " +str(calculateScore(z, 1903)))
        if calculateScore(z, 1903) == 1000:
            st.write("That's correct! Well done.")
        else:
            st.write("The correct year was 1903.")
    st.image("https://images.newscientist.com/wp-content/uploads/2019/07/26113900/first-powered-flight-fdx5jm_web.jpg", use_column_width=True)

# Fourth Image
    a = st.number_input(
        "### Choose the year this picture was taken!",
        min_value=1901,
        max_value=2000,
        label_visibility="collapsed",
        step = 1,
        key="button4"
    )  # time slider
    if st.button('Confirm', key='confirmbutton4'):
        st.write("You score " +str(calculateScore(a, 1942)))
        if calculateScore(a, 1942) == 1000:
            st.write("That's correct! Well done.")
        else:
            st.write("The correct year was 1942.")
    st.image("https://www.computerhope.com/cdn/eniac.jpg", use_column_width=True)


    # Last Image
    lastimage = st.number_input(
        "### Choose the year this picture was taken!",
        min_value=1901,
        max_value=2000,
        label_visibility="collapsed",
        step = 1,
        key="button5"
    )  # time slider
    if st.button('Confirm', key='confirmbutton5'):
        st.write("You score " +str(calculateScore(lastimage, 1942)))
        if calculateScore(lastimage, 1942) == 1000:
            st.write("That's correct! Well done.")
        else:
            st.write("The correct year was 1942.")
    st.image("https://upload.wikimedia.org/wikipedia/en/8/86/Einstein_tongue.jpg", use_column_width=True)


    st.write("## Your total score is " + str(calculateScore(x, 1980) + calculateScore(y, 1963) + calculateScore(lastimage, 1951) + calculateScore(z, 1903)))
    st.session_state['displayScore'] = str(calculateScore(x, 1980) + calculateScore(y, 1963) + calculateScore(lastimage, 1951) + calculateScore(z, 1903))





def twentyHard():
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
        st.write("You scored " + str(calculateScoreHard(x, 1980)))
        if calculateScoreHard(x, 1980) == 1000:
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
        st.write("You score " +str(calculateScoreHard(y, 1963)))
        if calculateScoreHard(y, 1963) == 1000:
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
        st.write("You score " +str(calculateScoreHard(z, 1903)))
        if calculateScoreHard(z, 1903) == 1000:
            st.write("That's correct! Well done.")
        else:
            st.write("The correct year was 1903.")
    st.image("https://images.newscientist.com/wp-content/uploads/2019/07/26113900/first-powered-flight-fdx5jm_web.jpg", use_column_width=True)

# Fourth Image
    a = st.number_input(
        "### Choose the year this picture was taken!",
        min_value=1901,
        max_value=2000,
        label_visibility="collapsed",
        step = 1,
        key="button4"
    )  # time slider
    if st.button('Confirm', key='confirmbutton4'):
        st.write("You score " +str(calculateScoreHard(a, 1942)))
        if calculateScoreHard(a, 1942) == 1000:
            st.write("That's correct! Well done.")
        else:
            st.write("The correct year was 1942.")
    st.image("https://www.computerhope.com/cdn/eniac.jpg", use_column_width=True)


    # Last Image
    lastimage = st.number_input(
        "### Choose the year this picture was taken!",
        min_value=1901,
        max_value=2000,
        label_visibility="collapsed",
        step = 1,
        key="button5"
    )  # time slider
    if st.button('Confirm', key='confirmbutton5'):
        st.write("You score " +str(calculateScoreHard(lastimage, 1942)))
        if calculateScoreHard(lastimage, 1942) == 1000:
            st.write("That's correct! Well done.")
        else:
            st.write("The correct year was 1942.")
    st.image("https://upload.wikimedia.org/wikipedia/en/8/86/Einstein_tongue.jpg", use_column_width=True)


    st.write("## Your total score is " + str(calculateScoreHard(x, 1980) + calculateScoreHard(y, 1963) + calculateScoreHard(lastimage, 1951) + calculateScore(z, 1903)))
    st.session_state['displayScore'] = str(calculateScoreHard(x, 1980) + calculateScoreHard(y, 1963) + calculateScoreHard(lastimage, 1951) + calculateScore(z, 1903))



