#!/usr/bin/env python

import sys


for line in sys.stdin:
        #strip each line
        line = line.strip()
        #split the line after each tab
        data = line.split("\t")
        
        ip1, sec1, sec2, sec3 = data
        sec1 = float(sec1)
        sec2 = float(sec2)
        sec3 = float(sec3)
         
        if ((sec1*2 <= sec2) and (sec2*2 <= sec3)):
            print('%s\t%s' % (ip1, 1))