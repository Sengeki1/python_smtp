import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.message import EmailMessage
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from typing import Union, List
from email import encoders

class MAIL:
    def __init__(self, 
                 server="smtp.gmail.com", 
                 context=ssl.create_default_context(),
                 port=465):
        
        self.server = server
        self.context = context
        self.port = port

        self.create_server()

    def create_server(self):
        self.smtp = smtplib.SMTP_SSL(self.server, self.port, context=self.context)

    def format_attachment(self, 
                          file):
        
        format = MIMEBase("application", "octet-stream") # generic binary stream, which means it’s suitable for any file type
        format.set_payload(file.read())
        encoders.encode_base64(format) # transmit binary data as text
        format.add_header("Content-Disposition", f"attachment; filename={file.name}")

        self.email.attach(format)
    
    def send(self,
            sender,
            app_password,
            receiver,
            subject,
            body,
            file_path: Union[str, List[str]]=None):
        
        self.smtp.login(sender, app_password)

        self.email = MIMEMultipart() if file_path else EmailMessage()
        self.email['From'] = sender
        self.email['To'] = receiver
        self.email['Subject'] = subject

        if not file_path:
            self.email.set_content(body)
            self.smtp.sendmail(sender, receiver, self.email.as_string())
        else:
            self.email.attach(MIMEText(body, "plain"))

            if isinstance(file_path, str):
                with open(file_path, "rb") as file:
                    self.format_attachment(file)
            else:
                for path in file_path:
                    with open(path, "rb") as file:
                        self.format_attachment(file)
            self.smtp.sendmail(sender, receiver, self.email.as_string())

        self.smtp.close()


