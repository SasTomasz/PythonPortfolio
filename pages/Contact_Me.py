import streamlit as st

import mail_sender

mail_was_sent_message = "Your message was sent successfully"
mail_was_not_sent_message = ("There were a problem with sending Your email. "
                             "Try again or try it later")

st.markdown("<h1 style='text-align: center;'>Contact me</h1>",
            unsafe_allow_html=True)

with st.form("contact_form", clear_on_submit=True):
    email = st.text_input("Your email address")
    message = st.text_area("Your message")
    submitted = st.form_submit_button("Submit")

    if submitted:
        mail_sender.set_email_content(email, message)
        is_sent = mail_sender.send_email()
        if is_sent:
            st.write(mail_was_sent_message)
        else:
            st.write(mail_was_not_sent_message)
