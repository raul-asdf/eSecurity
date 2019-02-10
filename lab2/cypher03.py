from Crypto.Cipher import AES
import hashlib
import sys
import binascii
import base64
import Padding

try:
    cipher = sys.argv[1]
    decode = sys.argv[2]
except:
    print "No params entered"
    sys.exit(1)


def encrypt(plaintext,key, mode):
  encobj = AES.new(key,mode)
  return(encobj.encrypt(plaintext))

def decrypt(ciphertext,key, mode):
  encobj = AES.new(key,mode)
  return(encobj.decrypt(ciphertext))

passwords = ["hello","ankle","changeme","123456"]

if decode in ["base64", "hex"]:
    if decode == "base64":
      ciphertext = base64.decodestring(cipher)
    else:
      ciphertext = binascii.unhexlify(cipher)
else:
    print "decoding format not supported"

for password in passwords:
  key = hashlib.sha256(password).digest()
  print "Password: ", password
  print " "
  try:
    plaintext = decrypt(ciphertext,key,AES.MODE_ECB)
    print plaintext
    plaintext = Padding.removePadding(plaintext,mode='CMS')
    print " decrypt: "+plaintext
  except:
    print "something went wrong"