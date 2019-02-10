#!/usr/bin/env  python

import passlib.hash
from commands import getoutput as gt

### salt="PkWj6gM4"
salt="cL0XMc1"

words=["changeme", "123456", "password"]

for word in words:
    print "APR1:"+passlib.hash.apr_md5_crypt.encrypt(word, salt=salt)

for word in words:
    print gt("openssl passwd -apr1 -salt "+ salt+" "+ word)