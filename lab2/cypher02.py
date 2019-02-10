from Crypto.Cipher import AES
import hashlib
import sys
import binascii
import base64
import Padding

try:
    password = sys.argv[1]
    cipher = sys.argv[2]
    decode = sys.argv[3]
except:
    print "No params entered"
    sys.exit(1)


def encrypt(plaintext,key, mode):
  encobj = AES.new(key,mode)
  return(encobj.encrypt(plaintext))

def decrypt(ciphertext,key, mode):
  encobj = AES.new(key,mode)
  return(encobj.decrypt(ciphertext))

key = hashlib.sha256(password).digest()

if decode in ["base64", "hex"]:
  if decode == "base64":
    ciphertext = base64.decodestring(cipher)
  else:
    ciphertext = binascii.unhexlify(cipher)
else:
  print "decoding format not supported"
  
plaintext = decrypt(ciphertext,key,AES.MODE_ECB)
print plaintext

plaintext = Padding.removePadding(plaintext,mode='CMS')
print " decrypt: "+plaintext