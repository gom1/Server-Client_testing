#!/usr/bin/python
import socket

TCP_IP = 'localhost'
TCP_PORT = 5037
BUFFER_SIZE = 1024


if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    print 'connected'
    s.send('adb logcat')
    data = s.recv(BUFFER_SIZE)
    print data
    s.close()

