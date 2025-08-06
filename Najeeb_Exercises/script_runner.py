# main_script.py
from email_sender import get_credentials, compose_email, send_email

def main():
    email, password = get_credentials()
    subject = "Welcome Address from Oyinlola's Email Sender"
    body = """
This is to show the depth of my research on using SMTPLIB and MIMEMultiPart and MIMEText.

I used a modular approach by enclosing all my variables in functions and secret keys in a dotenv file.

I also faced a struggle in thinking out this whole code but with the help of stack overflow and medium articles, i was able to overcome.
"""
    sender = email
    receivers = ["oyinlolaalasho95@gmail.com", "promise.chinonso@jadasquad.com", "joseph.fadero@jadasquad.com", "favour.atane@jadasquad.com"]
    message = compose_email(subject, body, sender, receivers)

    # Send email using the server, port, and credentials
    send_email("smtp.gmail.com", 465, receivers, message, email, password)

if __name__ == "__main__":
    main()