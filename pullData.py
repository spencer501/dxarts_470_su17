"""
File for pulling in data and remapping for export
Modeled after: https://wikitech.wikimedia.org/wiki/EventStreams
"""

# Import libraries
import json
from sseclient import SSEClient as EventSource

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
            sizeDiff = newSize - oldSize
            
            numChanges = numChanges + 1
            
            aveDiff = (aveDiff * (numChanges - 1) + abs(sizeDiff))/numChanges
            
            if (abs(sizeDiff) > maxDiff):
                maxDiff = abs(sizeDiff)
            
            
            # Logging details
            print(oldSize, '->', newSize, '=', 
                  'Diff:', sizeDiff, '\t',
                  'Type:', change['type'], '\n',
                  'Title:', change['title'], '\n',
                  'Average:', aveDiff,
                  'Max:', maxDiff, '\n')
            
            
            
            
