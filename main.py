import pandas
import streamlit as st

import logger_utils

logger = logger_utils.logger

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

col3, col4 = st.columns(2)

df = pandas.read_csv('./data.csv', sep=';')
half_of_rows = len(df.axes[0]) // 2

with col3:
    for index, row in df[:half_of_rows].iterrows():
        st.title(row['title'])
        st.write(row['description'])
        st.image(f"./images/{row['image']}")

        # Adds link to the working app
        if str(row['app_url']) != 'nan':
            st.write(f"[Working App]({row['app_url']})")

        st.write(f"[Source code]({row['url']})")

with col4:
    for index, row in df[half_of_rows:].iterrows():
        st.title(row['title'])
        st.write(row['description'])
        st.image('./images/' + row['image'])

        # Adds link to the working app
        if str(row['app_url']) != 'nan':
            st.write(f"[Working App]({row['app_url']})")

        st.write(f"[Source code]({row['url']})")
