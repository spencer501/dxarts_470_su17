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
changeType = 'edit'

for event in EventSource(url):
    
    if (event.event == 'message'):
        
        try:
            change = json.loads(event.data)
        except ValueError:
            continue
        
        if (change['wiki'] == wiki and
            change['type'] == changeType):
            
            oldSize = change['revision']['old']
            newSize = change['revision']['new']
            sizeDiff = newSize - oldSize
            
            print('Old size:', oldSize, 
                  'New size:', newSize, 
                  'Diff:', sizeDiff)
