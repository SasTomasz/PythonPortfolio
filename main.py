import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with open('./my_bio.txt', 'r') as file:
    bio = file.read()

with col1:
    st.image('./images/my_photo.jpg')

with col2:
    st.title("Tomasz Sas")
    st.write(bio)

contact_message = "Below you can find some of the apps I have build in Python. Feel free to contact me!"
st.write(contact_message)
