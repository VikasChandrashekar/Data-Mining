#!/usr/bin/env python

import sys


totalSeconds = 0
oldCombo=None
comboCount=0

for line in sys.stdin:
        #strip each line
        line = line.strip()
        #split the line after each tab
        data = line.split("\t")
         
        website,date,seconds = data
        thisCombo = website + "\t" + date
         
        if oldCombo and oldCombo != thisCombo:
            print('%s\t%s' % (oldCombo, float(totalSeconds/comboCount)))
            totalSeconds=0
            comboCount=0
                 
        oldCombo=thisCombo
        comboCount += 1
        totalSeconds += float(seconds)
        
if oldCombo != None:
    print('%s\t%s' % (oldCombo, float(totalSeconds/comboCount)))