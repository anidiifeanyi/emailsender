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