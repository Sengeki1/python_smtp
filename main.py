import smtplib, ssl
import os
from dotenv import load_dotenv
from email.message import EmailMessage

load_dotenv()

smtp_server = "smtp.gmail.com"
context=ssl.create_default_context()
port = 465

sender = os.getenv("EMAIL_SENDER")
app_password = os.getenv("APP_PASSWORD")
receiver = os.getenv("EMAIL_RECEIVER")

body = """
Hello from Python
"""

email = EmailMessage()
email['From'] = sender
email['To'] = receiver
email['Subject'] = "Test"
email.set_content(body)

with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender, app_password)
    server.sendmail(sender, receiver, email.as_string())
