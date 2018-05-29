#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 29 15:02:16 2018

@author: manish
"""

import smtplib
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("as955919@gmail.com", "ManIsh@123")
 
msg = "YOUR MESSAGE!"
server.sendmail("as955919@gmail.com", "mk60991@gmail.com", msg)
server.quit()
