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
    activeImage = 'https://upload.wikimedia.org/wikipedia/commons/8/81/Bundesarchiv_DVM_10_Bild-23-61-17%2C_Untergang_der_%22Lusitania%22.jpg'
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
        st.write("You scored " + str(calculateScoreHard(x, 1915)))
        if calculateScoreHard(x, 1915) == 1000:
            st.write("That's correct! Good job.")
        else:
            st.write("The correct year was 1915")
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
        st.write("You score " +str(calculateScoreHard(y, 1961)))
        if calculateScoreHard(y, 1961) == 1000:
            st.write("That's correct! Well done.")
        else:
            st.write("The correct year was 1961.")
    st.image("https://upload.wikimedia.org/wikipedia/commons/6/63/Attack_near_Playa_Giron._April_19%2C_1961._-_panoramio.jpg", use_column_width=True)

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
        st.write("You score " +str(calculateScoreHard(z, 1980)))
        if calculateScoreHard(z, 1980) == 1000:
            st.write("That's correct! Well done.")
        else:
            st.write("The correct year was 1980.")
    st.image("https://cdn.britannica.com/73/205873-050-97D227A2/Lech-Walesa-workers-trade-union-Solidarity-Poland-August-26-1980.jpg", use_column_width=True)

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
        if calculateScoreHard(a, 1947) == 1000:
            st.write("That's correct! Well done.")
        else:
            st.write("The correct year was 1947.")
    st.image("https://images.immediate.co.uk/production/volatile/sites/7/2022/08/GettyImages2666858-94ff777.png", use_column_width=True)


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
        st.write("You score " +str(calculateScoreHard(lastimage, 1915)))
        if calculateScoreHard(lastimage, 1915) == 1000:
            st.write("That's correct! Well done.")
        else:
            st.write("The correct year was 1942.")
    st.image("https://upload.wikimedia.org/wikipedia/commons/d/d9/RMS_Lusitania_coming_into_port%2C_possibly_in_New_York%2C_1907-13-crop.jpg", use_column_width=True)


    st.write("## Your total score is " + str(calculateScoreHard(x, 1980) + calculateScoreHard(y, 1963) + calculateScoreHard(lastimage, 1915) + calculateScoreHard(z, 1903) + calculateScoreHard(a, 1942)))
    st.session_state['displayScore'] = str(calculateScoreHard(x, 1980) + calculateScoreHard(y, 1963) + calculateScoreHard(lastimage, 1951) + calculateScoreHard(z, 1903))



