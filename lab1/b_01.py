#!/usr/bin/env  python

import sys

try:
    n1 = int(sys.argv[1])
    n2 = int(sys.argv[2])
except:
    print "No numbers entered"
    sys.exit(1)

def gcd(no1, no2):
    while no2 is not 0:
        (no1, no2) = (no2, no1 % no2)
    return no1

print gcd(n1, n2)

#print ngcd