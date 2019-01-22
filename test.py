
# Import libraries
from time import sleep
import serial
import struct
from random import randint

# Create Serial object
port = 'COM5'
baudrate = 9600
ser = serial.Serial(port, baudrate, timeout = 1)

# Make sure Serial port is open and give it time to reset the connection
if ser.isOpen():
     print(ser.name + ' is open...')
     sleep(3)
 
while True:

    val = randint(1, 4)
    
    ser.write(struct.pack('>B', val))
    print('Output:', val)
    
    sleep(1)

# Close the Serial connection so it can be used by other processes
ser.close()
