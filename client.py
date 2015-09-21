import time
from socket import *

HOST = '192.168.0.3'
PORT = 8952
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpclisock = socket(AF_INET, SOCK_STREAM)
tcpclisock.connect(ADDR)

while True:
    data = raw_input()
    if not data:
        break
    tcpclisock.send(data)
    data = tcpclisock.recv(BUFSIZ)
    print data
    if not data:
        break
    print data

tcpclisock.close()