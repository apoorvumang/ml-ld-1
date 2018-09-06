#!/usr/bin/python
import sys
for myline in sys.stdin:
    myline = myline.strip()
    words = myline.split()
    for myword in words:
        print '%s\t%s' % (myword, 1)
