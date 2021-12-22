from tdc_falcon import generate_keypair, sign, verify, priv_to_pub
import os
import binascii
import hashlib
import time

time_change = time.time()
salt = bytes.fromhex('aaef2d3f4d77ac66e9c5a6c3d8f921d1')
passwd = "Master Key".encode("utf8")

key = hashlib.pbkdf2_hmac('sha512', passwd, salt, iterations=500000, dklen=48)
print("Derived seed:", binascii.hexlify(key))

pub,priv=generate_keypair(key)
print("==== PUBKEY ====")
print(pub.hex())

print("==== PRIVKEY ====")
print(priv.hex())

print("==== PRIV TO PUB ====")
derived_pub=priv_to_pub(priv)
print(derived_pub.hex())

print("==== SIGNATURE ====")
sig=sign(priv, b'MESSAGE')
print(sig.hex())

print("==== VERIFY ====")
print(verify(pub,b'MESSAGE',sig))
print("==== VERIFY BAD MESSAGE ====")
print(verify(pub,b'BADMESSAGE',sig))

passwd1 = "Master Key 2".encode("utf8")

key1 = hashlib.pbkdf2_hmac('sha512', passwd1, salt, iterations=500000, dklen=48)
pub1,priv1=generate_keypair(key1)

sig1=sign(priv1,b'MESSAGE')
print("==== VERIFY BAD SIG ====")
print(verify(pub,b'MESSAGE',sig1))

print("==== VERIFY BAD PUB ====")
print(verify(pub1,b'MESSAGE',sig))

print(time.time()-time_change)

