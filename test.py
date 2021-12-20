from tdc_falcon import generate_keypair, sign, verify
import os
import binascii
import hashlib



salt = bytes.fromhex('aaef2d3f4d77ac66e9c5a6c3d8f921d1')
passwd = "Master Key".encode("utf8")

key = hashlib.pbkdf2_hmac('sha512', passwd, salt, iterations=500000, dklen=48)
print("Derived seed:", binascii.hexlify(key))

pub,priv=generate_keypair(key)
print("==== PUBKEY ====")
print(pub.hex())

print("==== PRIVKEY ====")
print(priv.hex())

print("==== SIGNATURE ====")
sig=sign(b'MESSAGE',priv)
print(sig.hex())

print("==== VERIFY ====")
print(verify(sig,b'MESSAGE',pub))
print("==== VERIFY BAD MESSAGE ====")
print(verify(sig,b'BADMESSAGE',pub))

passwd1 = "Master Key 2".encode("utf8")

key1 = hashlib.pbkdf2_hmac('sha512', passwd1, salt, iterations=500000, dklen=48)
pub1,priv1=generate_keypair(key1)

sig1=sign(b'MESSAGE',priv1)
print("==== VERIFY BAD SIG ====")
print(verify(sig1,b'MESSAGE',pub))

print("==== VERIFY BAD PUB ====")
print(verify(sig,b'MESSAGE',pub1))


