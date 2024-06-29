import smtplib
import os
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

class Mail:
    def __init__(self):
        load_dotenv()
        self.sender = os.getenv("USER")
        self.server = smtplib.SMTP("smtp.gmail.com", 587)
        self.server.starttls()
        self.server.login(self.sender, os.getenv("PASS"))

    def send_email(self, to, subject, content, image=None):
        msg = MIMEMultipart()
        msg["Subject"] = subject
        msg["From"] = self.sender
        msg["To"] = to
        msg.attach(MIMEText(content, "html"))

        if image is not None:
            with open(image, "rb") as f:
                image = MIMEImage(f.read())
                image.add_header("Content-ID", "<image1>")
                msg.attach(image)

        self.server.sendmail(self.sender, to, msg.as_string())
