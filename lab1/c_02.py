#!/usr/bin/env  python

import sys

# Mc mod p
try:
    M = int(sys.argv[1])
    c = int(sys.argv[2])
    p = int(sys.argv[3])
except:
    print "wrong params"
    sys.exit(1)

if p > 1:  
   for i in range(2, p//2): 
       if (p % i) == 0: 
           print p, "Not a prime number"
           break
   else: 
       print p, " <-- A prime number" 
       print M**c % p
  
else: 
   print p, "Not a prime number"