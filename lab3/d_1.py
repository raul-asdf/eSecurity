#!/usr/bin/env  python

import passlib.hash;

words=["napier", "foxtrot"]

for word in words:
    print "LM Hash:"+passlib.hash.lmhash.encrypt(word)
    print "NT Hash:"+passlib.hash.nthash.encrypt(word)