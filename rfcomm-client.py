
import bluetooth

bd_addr = "C0:33:5E:22:C3:68"
port = 5

sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.connect((bd_addr, port))

sock.send("hello!! 21321")

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