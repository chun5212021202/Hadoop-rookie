#!/usr/bin/env python
import sys
 
# maps words to their counts
time2count = {}
 
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
 
    # parse the input we got from mapper.py
    date , clock , count = line.split('\t', 2)
    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        continue

    try:
        time2count[(date,clock)] = time2count[(date,clock)] + count
    except:
        time2count[(date,clock)] = count
 
# write the tuples to stdout
# Note: they are unsorted

for time in time2count.keys():
    print '%s\t%s\t%s' % (time[0] , time[1] , time2count[time] )