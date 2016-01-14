#!/usr/bin/env python
#Copyright (c) Kieran Boyle

import socket
#INET = internet
#STREAM = TCP
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clientSocket.connect(("www.googe.com",80))
request = "GET / HTTP/1.0\n\n"
clientSocket.sendall(request)
response =bytearray()
done = False
while True:
	part = clientSocket.recv(1024)
	if(part):
		response.extend(part)
	else:
		break
print response
