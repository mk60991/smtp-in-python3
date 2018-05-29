#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 29 15:17:09 2018

@author: manish
"""

import sys
import os
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
 
fromaddr = "as955919@gmail.com"
toaddr = "mk60991@gmail.com"                                              #EMAIL ADDRESS YOU SEND TO
 
msg = MIMEMultipart()
 
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "smtp basic email with attachment"
 
body = "hello bro, myself manish kumar from adhoc network and doing training on ML"
 
msg.attach(MIMEText(body, 'plain'))
 
filename = "google.jpg"
attachment = open("/home/manish/forsk ml/google.jpg", "rb")
 
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
msg.attach(part)
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "ManIsh@123")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
print("successfully sent email")
server.quit()