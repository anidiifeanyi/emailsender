from email.message import EmailMessage
from dotenv import password
import ssl
import smtplib

# Email credentials
email_sender = 'Your email'
email_password = password
email_receiver = ''

# email body
subject = "Dont forget to subscribe"
body = """
When you watch a video, please hit subscribe
"""

# instant of email message
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em[' subject'] = subject
em.set_content(body)

# Configure SMTP Sender
context = ssl.create_default_context()

with smtplib.SMTP_SSL( 'smtp.gmail.com' , 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())