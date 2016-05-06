#!/usr/bin/env python

import sys


for line in sys.stdin:
    line = line.strip()
    data = line.split("\t")
    ip,spikes=data
    print('%s\t%s' % (ip,spikes))