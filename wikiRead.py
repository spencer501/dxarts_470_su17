

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


class WikiReader:
    
    def __init__(self, wikiName = 'enwiki'):
        
        self.__url = 'https://stream.wikimedia.org/v2/stream/recentchange'
        self.__changeTypes = {'new', 'edit'}
        self.wiki = wikiName
        
    def streamChanges(self, serial, stopper):
        
        for event in EventSource(self.__url):
    
            if (event.event == 'message'):
                
                try:
                    change = json.loads(event.data)
                except ValueError:
                    continue
                
                if (change['wiki'] == self.wiki and
                    change['type'] in self.__changeTypes):
                    
                    oldSize = change['length']['old'] or 0
                    newSize = change['length']['new']
                    sizeDiff = abs(newSize - oldSize)
                        
                    scaleValue = scaleSize(sizeDiff)
                    
                    serial.write(struct.pack('>B', scaleValue))
                    
                    print('Size:', sizeDiff, 'Output:', scaleValue)
        
    
        
