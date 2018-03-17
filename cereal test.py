import serial
import time
ser = serial.Serial("COM3", 9600)
var = 55
var = str(var)
while True:
    try:
        print(var)
        ser.write(bytes(var.encode('ascii')))
        print(ser.readline())
        time.sleep(1)
    except ser.SerialTimeoutException:
        print(('Data could not be read'))
