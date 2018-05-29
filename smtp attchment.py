#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 29 13:18:52 2018

@author: manish
"""

#import email
#'dir' to show all function in 'email'
#dir(email)

#Create an SMTP object for connection to the server.
#Log in to your account.
#Define your message headers and login credentials.
#Create a MIMEMultipart message object and attach the relevant headers to it, i.e. From, To, and Subject.
#Read and attach the image to the message MIMEMultipart object.
#Finally, send the message.

#create and send email with attachment

# send_attachment.py
# import necessary packages
from email.mime.multipart import MIMEMultipart
from email.MIMEImage import MIMEImage
from email.mime.text import MIMEText
import smtplib
 
# create message object instance
msg = MIMEMultipart()
 
 
# setup the parameters of the message
password = "ManIsh@123"
msg['From'] = "as955919@gmail.com"
msg['To'] = "mk60991@gmail.com"
msg['Subject'] = "Photos"
 
# attach image to message body
msg.attach(MIMEImage(file("google.jpg").read()))
 
 
# create server
server = smtplib.SMTP('smtp.gmail.com: 587')
 
server.starttls()
 
# Login Credentials for sending the mail
server.login(msg['From'], password)
 
 
# send the message via the server.
server.sendmail(msg['From'], msg['To'], msg.as_string())
 
server.quit()
 
print ("successfully sent email to %s:" % (msg['To']))
