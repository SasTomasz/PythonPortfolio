import streamlit as st

st.markdown("<h1 style='text-align: center;'>Contact me</h1>", unsafe_allow_html=True)

with st.form("contact_form"):
    email = st.text_input("Your email address")
    message = st.text_area("Your message")
    st.form_submit_button("Submit")
