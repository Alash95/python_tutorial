"""Work on an email sender, it takes in a message and returns an email to me"""

import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


def get_credentials():
    """Retrieve email and password credentials from environment variables.

    Returns:
        tuple: A tuple containing the email (str) and password (str) for the sender account.

    Note:
        Ensure that the .env file is present and contains the 'email' and 'password' variables.
    """

    email = os.environ.get("email")
    password = os.environ.get("password")
    return email, password


def compose_email(subject, body, sender, receivers):
    """Compose a multipart email message with specified content and headers.

    Args:
        subject (str): The subject line of the email.
        body (str): The plain text content/body of the email.
        sender (str): The sender's email address.
        receivers (list): List of recipient email addresses.

    Returns:
        MIMEMultipart: A configured email message object with headers and body attached.

    Note:
        The 'To' header is automatically joined from the receivers list using commas.
    """

    message = MIMEMultipart()
    message["From"] = sender
    message["To"] = ", ".join(receivers)
    message["Subject"] = subject

    message.attach(MIMEText(body, "plain"))
    return message


def connect_smtp_server(server, port):
    """Establish a secure SMTP connection to the specified server and port.

    Args:
        server (str): The SMTP server address (e.g., "smtp.gmail.com").
        port (int): The port number for the SMTP server (e.g., 465 for Gmail SSL).

    Returns:
        smtplib.SMTP: An authenticated SMTP connection object.

    Note:
        This function uses SMTP_SSL for secure connections. Ensure the port matches
        the server's SSL requirements (typically 465 for Gmail).
    """

    smtp_connection = smtplib.SMTP_SSL(server, port)
    return smtp_connection


def send_email(server, port, receivers, message, sender, password):
    """Send an email through an established SMTP connection.

    Args:
        smtp_connection (smtplib.SMTP): An authenticated SMTP connection object.
        receiver (list): List of recipient email addresses.
        message (MIMEMultipart): Pre-composed email message object with headers and content.
        sender (str): Sender's email address used for authentication.
        password (str): Sender's account password for SMTP authentication.

    Uses `with` to ensure the SMTP connection is closed automatically.
    """
    with smtplib.SMTP_SSL(server, port) as smtp_connection:
        try:
            smtp_connection.login(sender, password)
            smtp_connection.sendmail(
                sender, receivers,  message.as_string()
            )
            print("✅ Email sent successfully!")
        except Exception as e:
            print(f"❌ Failed to send email: {e}")
