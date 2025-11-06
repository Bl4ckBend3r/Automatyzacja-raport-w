import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from config import *

def send_email(report_path):
    msg = MIMEMultipart()
    msg['From'] = EMAIL_SENDER
    msg['To'] = ", ".join(EMAIL_RECEIVERS)
    msg['Subject'] = "Automatyczny raport sprzedażowy"

    body = MIMEText("W załączniku znajduje się dzisiejszy raport sprzedażowy.", 'plain')
    msg.attach(body)

    with open(report_path, "rb") as file:
        part = MIMEApplication(file.read(), Name=report_path.split('/')[-1])
    part['Content-Disposition'] = f'attachment; filename="{report_path.split('/')[-1]}"'
    msg.attach(part)

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.send_message(msg)
