'''
Encryption and decryption of user specified message using AES 256 encryption.
Module used in this program is "pyCrypto"
Install PyCrypto using the command "pip install pyCrypto"
'''
from Crypto.Cipher import AES
key = 'abcd1234abcd1234'                                          #This key can be 16, 24 or 32 bit

def encrypt(msg):
 obj = AES.new(key, AES.MODE_CBC, 'This is an IV456')
 ciphertext = obj.encrypt(msg*16)
 print ("Encrypted text = ",ciphertext)
 return ciphertext

def decrypt(ciph, mlen):
 obj2 = AES.new(key, AES.MODE_CBC, 'This is an IV456')
 x = obj2.decrypt(ciph)
 x = x[0:mlen]                                                     #Removing extra padding from decrpyted message
 print("Decrypted text = ",x.decode('utf-8'))

message = "Hi how are you doing today?" 
mlen = len(message)
cip = encrypt(message)
decrypt(cip, mlen)