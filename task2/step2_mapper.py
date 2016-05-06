#!/usr/bin/env python

from datetime import datetime
import sys

count = 0
data = []
for line in sys.stdin:
    data.append(line.strip())
    
    count += 1

    if count == 3:
        ip1, date1, sec1 = data[0].split('\t')
        ip2, date2, sec2 = data[1].split('\t')
        ip3, date3, sec3 = data[2].split('\t')
        if ip1 == ip2 and ip2 == ip3: 
            diff12 = (datetime.strptime(date2, '%Y-%m-%d') - datetime.strptime(date1, '%Y-%m-%d')).days
            diff23 = (datetime.strptime(date3, '%Y-%m-%d') - datetime.strptime(date2, '%Y-%m-%d')).days
            if diff12 == 1 and diff23 == 1:
                print('%s\t%s\t%s\t%s' % (ip1, sec1, sec2, sec3))
        
        data[0] = data[1]
        data[1] = data[2]
        del data[-1]
        
        count -= 1