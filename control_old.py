
# Import libraries
import time
import serial
import struct
import json
import math
from sseclient import SSEClient as EventSource

def scaleSize(inputSize):
    """Scale a given value.
    
    The return values is created using a logarithmic scale (base 10), with all
    decimal values truncated.
    
    args:
        
        inputSize -- number to be scaled
        
    returns:
        
        The truncated log10 value of the input
        
    """
    
    try:
        scaledValue = math.log10(inputSize)
        scaledValue = math.trunc(scaledValue)
    except ValueError:
        scaledValue = 0
    
    return scaledValue


# Create Serial object
port = 'COM5'
baudrate = 9600
ser = serial.Serial(port, baudrate, timeout = 1)

# Make sure Serial port is open and give it time to reset the connection
if ser.isOpen():
     print(ser.name + ' is open...')
     time.sleep(3)
 
    
# Parameters for stream source
url = 'https://stream.wikimedia.org/v2/stream/recentchange'
wiki = 'enwiki'
changeTypes = {'new', 'edit'}

# Scaling parameters
maxDiff = 0
aveDiff = 0
numChanges = 0

for event in EventSource(url):
    
    if (event.event == 'message'):
        
        try:
            change = json.loads(event.data)
        except ValueError:
            continue
        
        if (change['wiki'] == wiki and
            change['type'] in changeTypes):
            
            oldSize = change['length']['old'] or 0
            newSize = change['length']['new']
            sizeDiff = abs(newSize - oldSize)
                
            scaleValue = scaleSize(sizeDiff)
            
            ser.write(struct.pack('>B', scaleValue))
            
            print('Size:', sizeDiff, 'Output:', scaleValue)

# Close the Serial connection so it can be used by other processes
ser.close()
