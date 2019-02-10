#!/usr/bin/env  python

import hashlib
import passlib.hash
import sys

try:
    string = sys.argv[1]
    salt = sys.argv[2]
except:
    salt = "ZDzPE45C"
    string = "password"

print "PBKDF2 (SHA1):"+passlib.hash.pbkdf2_sha1.encrypt(string, salt=salt)
print "PBKDF2 (SHA256):"+passlib.hash.pbkdf2_sha256.encrypt(string, salt=salt)