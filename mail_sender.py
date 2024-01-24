import os
import smtplib
import ssl

from dotenv import load_dotenv

import logger_utils

load_dotenv()

logger = logger_utils.logger

host = 'smtp.gmail.com'
port = 587
login = os.getenv('LOGIN')
password = os.getenv('APP_PASSWORD')
email_receiver = os.getenv('MY_EMAIL')
message = """\
Subject: Hello from python
This is my first message sending with python code
"""

context = ssl.create_default_context()


def send_email(sender, receiver):
    try:
        server = smtplib.SMTP(host, port)
        server.starttls(context=context)
        server.login(login, password)
        server.sendmail(sender, receiver, message)
    except Exception as e:
        logger.error(e)
    finally:
        server.quit()


if __name__ == "__main__":
    send_email(login, email_receiver)
