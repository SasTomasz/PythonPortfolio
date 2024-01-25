import os
import smtplib
import ssl

from dotenv import load_dotenv

import logger_utils

load_dotenv()

logger = logger_utils.logger

host = 'smtp.gmail.com'
port = 587
password = os.getenv('APP_PASSWORD')
email_sender = os.getenv('LOGIN')
email_receiver = os.getenv('MY_EMAIL')
message = """\
Subject: Hello from python
This is a message sending with python code
"""

context = ssl.create_default_context()


def send_email():
    try:
        server = smtplib.SMTP(host, port)
        server.starttls(context=context)
        server.login(email_sender, password)
        server.sendmail(email_sender, email_receiver, message)
        server.quit()
        return True
    except Exception as e:
        logger.error(e)
        return False


def set_email_content(user_email, user_message):
    global message
    message = f"Subject: web-form from {user_email}\n{user_message}"


if __name__ == "__main__":
    send_email()