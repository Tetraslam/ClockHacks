import streamlit as st



index = 1
score = 0

def twenty():
    activeImage = 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5d/Berlinermauer.jpg/267px-Berlinermauer.jpg'
    st.write("# 20th Century")
    st.write("### Choose the year this picture was taken!")
    x = st.slider(
        "### Choose the year this picture was taken!",
        min_value=1901,
        max_value=2000,
        label_visibility="collapsed",
    )  # time slider
    st.image(activeImage, use_column_width=True)
    while index<3:
        if x == 1980:
                score+=1
                index+=1
        else:
            index+=1
        if index == 1:
            activeImage = 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/JFK_limousine.png/640px-JFK_limousine.png'
            if x==1963:
                score+=1
                index+=1
            else:
                index+=1
        if index == 2:
            activeImage = 'https://upload.wikimedia.org/wikipedia/en/8/86/Einstein_tongue.jpg'
            if x==1951:
                score+=1
                index+=1
            else:
                index+=1
    st.write("You scored " + score)
        
        
    


