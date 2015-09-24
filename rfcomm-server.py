#
# import bluetooth
#
# server_sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
#
# port = 1
# server_sock.bind(("",port))
# server_sock.listen(1)
#
# client_sock,address = server_sock.accept()
# print "Accepted connection from ",address
#
# data = client_sock.recv(1024)
# print "received [%s]" % data
#
# client_sock.close()
# server_sock.close()


import bluetooth

server_sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )

port = bluetooth.get_available_port( bluetooth.RFCOMM )
server_sock.bind(("",port))
server_sock.listen(1)
print "listening on port %d" % port

uuid = "08C2B2EF-7C87-3D00-0CDC-9A2ADC420BFF"
bluetooth.advertise_service( server_sock, "FooBar Service", uuid )

client_sock,address = server_sock.accept()
print "Accepted connection from ",address

data = client_sock.recv(1024)
print "received [%s]" % data

client_sock.close()
server_sock.close()