
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
