"""
File for pulling in data and remapping for export
Modeled after: https://wikitech.wikimedia.org/wiki/EventStreams
"""

# Import libraries
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
            
            numChanges = numChanges + 1
            
            aveDiff = (aveDiff * (numChanges - 1) + sizeDiff)/numChanges
            
            if (abs(sizeDiff) > maxDiff):
                maxDiff = abs(sizeDiff)
                
            scaleValue = scaleSize(sizeDiff)
            
            # Logging details
            print(oldSize, '->', newSize, '=', 
                  'Diff:', sizeDiff, '\t',
                  'Type:', change['type'], '\n',
                  'Title:', change['title'], '\n',
                  'Average:', aveDiff,
                  'Max:', maxDiff, '\n',
                  'Scaled:', scaleValue, '\n')
