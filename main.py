import os
from mail import MAIL
from dotenv import load_dotenv

load_dotenv()

sender = os.getenv("EMAIL_SENDER")
app_password = os.getenv("APP_PASSWORD")
receiver = os.getenv("EMAIL_RECEIVER")

body = """
Hello from Python
"""

mail = MAIL()
mail.send(sender, 
          app_password, 
          receiver,
          "Test",
          body)
