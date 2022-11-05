import streamlit as st





def twenty():
    index = 1
    score = 0
    confirmed = False
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
        finalx = x
    st.image(activeImage, use_column_width=True)
    if finalx == 1980:
            score+=1
            index+=1
    else:
        index+=1
    if index == 1:
        activeImage = 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/JFK_limousine.png/640px-JFK_limousine.png'
        if finalx==1963:
            score+=1
            index+=1
        else:
            index+=1
    if index == 2:
        activeImage = 'https://upload.wikimedia.org/wikipedia/en/8/86/Einstein_tongue.jpg'
        if finalx==1951:
            score+=1
            index+=1
        else:
            index+=1
    st.write("You scored " + str(score))
        
        
    


