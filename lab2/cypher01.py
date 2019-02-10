from Crypto.Cipher import AES
import hashlib
import sys
import binascii
import Padding

try:
    n1 = sys.argv[1]
    n2 = sys.argv[2]
except:
    print "No params entered"
    sys.exit(1)
val=n1
password = n2
plaintext = val
def encrypt(plaintext,key, mode):
  encobj = AES.new(key,mode)
  return(encobj.encrypt(plaintext))
def decrypt(ciphertext,key, mode):
  encobj = AES.new(key,mode)
  return(encobj.decrypt(ciphertext))
key = hashlib.sha256(password).digest()
plaintext = Padding.appendPadding(plaintext,blocksize=Padding.AES_blocksize,mode='CMS')
print "After padding (CMS): "+binascii.hexlify(bytearray(plaintext))
ciphertext = encrypt(plaintext,key,AES.MODE_ECB)
print "Cipher (ECB): "+binascii.hexlify(bytearray(ciphertext))
plaintext = decrypt(ciphertext,key,AES.MODE_ECB)
plaintext = Padding.removePadding(plaintext,mode='CMS')
print " decrypt: "+plaintext
plaintext=val