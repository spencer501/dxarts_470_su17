import time
import serial

# Create Serial object
port = 'COM5'
baudrate = 9600
ser = serial.Serial(port, baudrate, timeout = 1)

# Make sure Serial port is open and give it time to reset the connection
if ser.isOpen():
     print(ser.name + ' is open...')
     time.sleep(3)
     
 

# Close the Serial connection so it can be used by other processes
ser.close()