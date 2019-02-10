#!/usr/bin/env  python

import passlib.hash
from commands import getoutput as gt

salt="8sFt66rZ"

words=["changeme", "123456","password"]

for w in words:
    print "SHA1:"+passlib.hash.sha1_crypt.encrypt(w, salt=salt)
    print "SHA256:"+passlib.hash.sha256_crypt.encrypt(w, salt=salt)
    print "SHA512:"+passlib.hash.sha512_crypt.encrypt(w, salt=salt)

for w in words:
    print gt("htpasswd -nbs elpuffin " + w)