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
            
            print(oldSize, '->', newSize, '=', 
                  'Diff:', sizeDiff, '\t',
                  'Type:', change['type'], '\n',
                  'Title:', change['title'], '\n')
