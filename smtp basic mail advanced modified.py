#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 29 14:56:52 2018

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
toaddr = "mk60991@gmail.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "smtp with attachment"
 
body = "sir, myself amnish kumat from adhoc network learn=ing machine learning python"
                                               
msg.attach(MIMEText(body, 'plain'))
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "ManIsh@123")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
