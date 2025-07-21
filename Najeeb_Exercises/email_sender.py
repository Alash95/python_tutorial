"""Work on an email sender, it takes in a message and returns an email to me"""

import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

def get_credentials():
    email = os.environ.get("email")
    password = os.environ.get("password")
    return email, password

def compose_email(subject, body, sender, receivers):
    message = MIMEMultipart()
    message["From"] = sender
    message["To"] = ", ".join(receivers)
    message["Subject"] = subject

    message.attach(MIMEText(body, "plain"))
    return message

def connect_smtp_server(server, port):
    smtp_connection = smtplib.SMTP_SSL(server, port)
    # smtp_connection.starttls()
    return smtp_connection

def send_email(smtp_connection, receiver, message, sender, password):
    try:
        smtp_connection.login(sender, password)
        smtp_connection.sendmail(
            sender, receiver,  message.as_string()
        )
        print("✅ Email sent successfully!")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")

def close_connection(smtp_connection):
    smtp_connection.quit()

def main():
    # Load credentials function
    email, password = get_credentials()

    # compose emails function
    subject = "Welcome Address from Oyinlola's Email Sender"
    body = """
This is to show the depth of my research on using SMTPLIB and MIMEMultiPart 
and MIMEText.

I used a modular approach by enclosing all my variables in functions and
secret keys in a dotenv file.

I also faced a struggle in thinking out this whole code but with the help 
of stack overflow and medium articles, i was able to overcome.
"""

    sender = email
    receivers = ["oyinlolaalasho95@gmail.com", "promise.chinonso@jadasquad.com", "joseph.fadero@jadasquad.com", "favour.atane@jadasquad.com"]

    message = compose_email(subject, body, sender, receivers)

    # connect function
    smtp_connection = connect_smtp_server("smtp.gmail.com", 465)

    # send email function
    send_email(smtp_connection, receivers, message, email, password)

    # close connection function
    close_connection(smtp_connection)
if __name__ == "__main__":
    main()
    