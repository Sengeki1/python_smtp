import smtplib, ssl
import os
from dotenv import load_dotenv

load_dotenv()

smtp_server = "smtp.gmail.com"
context=ssl.create_default_context()
port = 465

sender = os.getenv("EMAIL_SENDER")
app_password = os.getenv("APP_PASSWORD")
receiver = os.getenv("EMAIL_RECEIVER")

with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender, app_password)
    server.sendmail(sender, receiver, "Subject: test\r\n\r\nHello from Python")
