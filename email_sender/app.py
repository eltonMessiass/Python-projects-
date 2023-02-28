# go over our gmail account and setup 2 factor authentication
# generate app password
# creatw a function to send the email

from email.message import EmailMessage
import ssl
import smtplib

email_sender = 'guambee43@gmail.com'
email_password = 'sdoabuoebjfavgbp'

email_receiver = 'wific33268@wifame.com'

subject = "Hi Elton"

body = """ 
Hello, Elton Project
"""

em = EmailMessage()
em['from'] = email_sender
em['to'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465,context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())


