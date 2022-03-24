import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import credentials

message=MIMEMultipart()
message["from"]="Zartab Nakhwa"
message["to"]="nzartab@gmail.com"
message["subject"]="test Mail from JP Python Batch"
body="This is a an email body!!"
message.attach(MIMEText(body))

with smtplib.SMTP(host="smtp.gmail.com",port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("codewithz21@gmail.com",credentials.get_password())
    smtp.send_message(message)
    print("Sent...")
