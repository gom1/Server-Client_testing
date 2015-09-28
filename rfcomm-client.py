
import bluetooth

bd_addr = "C0:33:5E:22:C3:68"
port = 5

sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.connect((bd_addr, port))

sock.send("hello!! 21321")

sock.close()
