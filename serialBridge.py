"""
Python script that sends random numbers over Serial which correspond to LEDs on
an Arduino
"""

# Import libraries
import time
import random as r
import serial
import struct

# Create Serial object
port = 'COM5'
baudrate = 9600
ser = serial.Serial(port, baudrate, timeout = 1)

# Make sure Serial port is open and give it time to reset the connection
if ser.isOpen():
     print(ser.name + ' is open...')
     time.sleep(3)

# Send random data over Serial to Arduino
count = 0
while count < 10:
    val = r.randint(1, 4)
    ser.write(struct.pack('>B', val))
    print("LED value:", ser.readline().decode('ascii'))
    count = count + 1
    
# Close the Serial connection so it can be used by other processes
ser.close()
