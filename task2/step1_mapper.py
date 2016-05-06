#!/usr/bin/env python

from datetime import datetime
import sys


for line in sys.stdin:
        # strip each line
        line = line.strip()
        data = line.split("\t")
        website, login, logout = data
        date = datetime.strptime(logout.split(" ")[0], '%Y-%m-%d').date()
        time1 = datetime.strptime(login, '%Y-%m-%d %H:%M:%S')
        time2 = datetime.strptime(logout, '%Y-%m-%d %H:%M:%S')
        secondstime = (time2 - time1).seconds
        print('%s\t%s\t%s' % (website, date.__str__(), secondstime))
          
