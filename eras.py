import streamlit as st


def twenty():
    st.write("# 20th Century")
    st.write("### Choose the year this picture was taken!")
    x = st.slider(
        "### Choose the year this picture was taken!",
        min_value=1901,
        max_value=2000,
        label_visibility="collapsed",
    )  # time slider

    st.write(x)

    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5d/Berlinermauer.jpg/267px-Berlinermauer.jpg",
        use_column_width=True,
    )