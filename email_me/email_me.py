#!/Users/edgar/anaconda3/bin/python

import os
import arrow
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Get credentials.
filepath = os.path.join(os.path.dirname("__file__"), "credentials", "email_credentials.txt")
with open(filepath, "r") as f:
    username, password = f.readlines()

# Set up smtp object.
smtp_object = smtplib.SMTP("smtp.gmail.com", 587)
smtp_object.ehlo()
smtp_object.starttls()
smtp_object.login(username, password)

# Message details.
msg = MIMEMultipart("alternative")
msg["Subject"] = f"DAILY TASKS: {'/'.join(reversed(str(arrow.utcnow().date()).split('-')))}"
msg["From"] = username
msg["To"] = username

# Message creation.
plaintext = "This is plaintext!"
html = """\
<h1 style='color:red'>This is an example email!</h1>
"""

part1 = MIMEText(plaintext, "plain")
part2 = MIMEText(html, "html")

msg.attach(part1)
msg.attach(part2)

# Message sent.
smtp_object.send_message(msg, username, username)

# Quit.
smtp_object.quit()
