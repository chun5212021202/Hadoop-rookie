#!/usr/bin/env python
import sys
 
month = {}
month['Mar'] = 3

#--- get all lines from stdin ---
for line in sys.stdin:
    #--- remove leading and trailing whitespace---
    line = line.strip()
    time = line[line.find('[')+1 : line.find(']')]
    time = time[:time.find('-')]
    time = time.strip()

    date  = time.split(':' , 1)[0]
    clock = time.split(':' , 1)[1]

    date  = date.split('/')
    clock = clock.split(':')

    date_string = str(date[2])+'-'+str(month[date[1]])+'-'+str(date[0])
    clock_string= str(clock[0])+':00:00.000'
    
    #--- output tuples [word, 1] in tab-delimited format---
    print '%s\t%s\t%s' % (date_string , clock_string , "1")