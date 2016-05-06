#!/usr/bin/env python
import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
        #strip each line
        line = line.strip()
        #split the line after each tab
        data = line.split("\t")
        #all the split attributes are put into different variables
        store,dep,date,weekly_sales = data
        #the date is split after each '-'
        newdate=date.split('-')
        #split attributes are put into different variables
        year,month,day = newdate
        #only required feilds are displayed for mapper
        print('%s\t%s\t%s' % (dep, year, weekly_sales))
        