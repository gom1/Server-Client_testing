
import bluetooth

bd_addr = "2C:54:CF:79:CC:24"
port = 5

sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.connect((bd_addr, port))

done = False
while done != True:
    temp = raw_input("Message: ")
    sock.send(temp)
    incoming = sock.recv(1024)
    print incoming

    if temp == "1":
        done=False
        print "hi"



sock.close()

#
# import sys
# import bluetooth
#
# target_address = "C0:33:5E:22:C3:68"
# service_matches = bluetooth.find_service(address=target_address)
#
# if len(service_matches) == 0:
#     print "couldn't find the FooBar service"
#     sys.exit(0)
#
# first_match = service_matches[0]
# port = first_match["port"]
# name = first_match["name"]
# host = first_match["host"]
# print port, name, host
#
# print "connecting to \"%s\" on %s" % (name, host)
#
# sock=bluetooth.BluetoothSocket(bluetooth.RFCOMM)
# sock.connect((host, 1))
# sock.send("hello!!")
# sock.close()