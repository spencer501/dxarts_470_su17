# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 01:07:41 2017

@author: spenc
"""

# Import libraries
import time
import serial
import struct
import json
from sseclient import SSEClient as EventSource

def scaleSize(inputSize):
    """
    scaleSize takes in a given number (preferably int <= 0) and returns a new,
    scaled value.
        
        inputSize: Number to be scaled
        
        Returns: A scaled value from 1 to 4, or 5 if the input is out of the
            intended range       
    """
    
    if (inputSize // 10 == 0):
        scaledValue = 1
    elif (inputSize // 100 == 0):
        scaledValue = 2
    elif (inputSize // 1000 == 0):
        scaledValue = 3
    elif (inputSize // 10000 == 0):
        scaledValue = 4
    else:
        scaledValue = 5

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

            

