import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, message, from_email, to_email, password):
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, password)
    text = msg.as_string()
    server.sendmail(from_email, to_email, text)
    server.quit()

subject = "Form submission"
message = "Hello,\n\nThis is a test email from your HTML form."
from_email = "acheseupet@gmail.com"
to_email = "fontana.rafael@gmail.com"
password = "yourpassword"

send_email(subject, message, from_email, to_email, password)