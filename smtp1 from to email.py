#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 29 12:53:53 2018

@author: manish
"""

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
 
# create message object instance
msg = MIMEMultipart()
 
 
message = "Thank you"
 
# setup the parameters of the message
password = "ManIsh@123"
msg['From'] = "as955919@gmail.com"
msg['To'] = "mk60991@gmail.com"
msg['Subject'] = "manish adhoc"
 
# add in the message body
msg.attach(MIMEText(message, 'plain'))
 
#create server
server = smtplib.SMTP('smtp.gmail.com: 587')
 
server.starttls()
 
# Login Credentials for sending the mail
server.login(msg['From'], password)
 
 
# send the message via the server.
server.sendmail(msg['From'], msg['To'], msg.as_string())
 
server.quit()
 
print ("successfully sent email to %s:" % (msg['To']))