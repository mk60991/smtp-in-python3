#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 29 16:26:20 2018

@author: manish
"""
# 1 st method old method of google to send message to receiver 
#by using "username" and "password"
#it use .SSL method oldest method
import smtplib

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login("ish manish", "ManIsh@123")
server.sendmail(
  "as955919@gmail.com", 
  "mk60991@gmail.com", 
  "this message is from python")
server.quit()


#2 nd method modified version to send email to receiver
#using "email-od" and "password"

import smtplib
gmail_user = "as955919@gmail.com"
gmail_pwd = "ManIsh@123"
TO = 'mk60991@gmail.com'
SUBJECT = "Testing sending using gmail"
TEXT = "Testing sending mail using gmail servers"
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login(gmail_user, gmail_pwd)
BODY = '\r\n'.join(['To: %s' % TO,
        'From: %s' % gmail_user,
        'Subject: %s' % SUBJECT,
        '', TEXT])

server.sendmail(gmail_user, [TO], BODY)
print ('email sent')