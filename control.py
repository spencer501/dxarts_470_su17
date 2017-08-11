import time
import serial
import wikiRead

# Create Serial object
port = 'COM5'
baudrate = 9600
ser = serial.Serial(port, baudrate, timeout = 1)

print('Trying to open serial communication on ' + ser.name)

# Make sure Serial port is open and give it time to reset the connection
if ser.isOpen():
    time.sleep(3)
    print(ser.name + ' is open...')
    time.sleep(1)

# Start streaming wiki changes
wr = wikiRead.WikiReader()

wr.streamChanges(ser, "end")
 

# Close the Serial connection so it can be used by other processes
ser.close()