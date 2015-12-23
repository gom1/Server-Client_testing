
import bluetooth

watson_2_for_rosie_bd_addr = "2C:54:CF:79:CC:24"
brandons_watson_5_bd_addr = "CC:FA:00:55:F7:7E"
brandons_watson_6_bd_addr = "0C:48:85:94:37:B1"

bd_addr = "2C:54:CF:79:CC:24"
port = 5

sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.connect((brandons_watson_5_bd_addr, port))

temp = raw_input("Message: ")
sock.send(temp)


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
