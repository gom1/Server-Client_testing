import socket
from socket import*
from time import ctime

HOST = '192.168.1.77'
PORT = 8952 #21567
BUFSIZ = 1024
ADDR =(HOST, PORT)

tcpsersock = socket(AF_INET, SOCK_STREAM)
tcpsersock.bind(ADDR)
tcpsersock.listen(5)

while True:
    print("waiting for connection...")
    tcpclisock, addr = tcpsersock.accept()
    print("...Connected from: "),addr

    while True:
        data = tcpclisock.recv(BUFSIZ)
        print data
        if not data:
            break
        tcpclisock.send('[%s] %s' %(ctime(), data))

    tcpclisock.close()
tcpsersock.close()