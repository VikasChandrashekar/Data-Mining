#!/usr/bin/env python

import sys


totalSpikes = 0
oldIP = None

for line in sys.stdin:
        # strip each line
        line = line.strip()
        # split the line after each tab
        data = line.split("\t")
         
        thisIP, spikes = data
        
         
        if oldIP and oldIP != thisIP:
            print('%s\t%s' % (oldIP, int(totalSpikes)))
            totalSpikes = 0
                 
        oldIP = thisIP
        totalSpikes += float(spikes)
        
if oldIP != None:
    print('%s\t%s' % (oldIP, int(totalSpikes)))
