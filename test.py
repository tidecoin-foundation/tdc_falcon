from tdc_falcon import generate_keypair
import os
import binascii
import hashlib



salt = bytes.fromhex('aaef2d3f4d77ac66e9c5a6c3d8f921d1')
passwd = "Master Key".encode("utf8")

key = hashlib.pbkdf2_hmac('sha512', passwd, salt, iterations=500000, dklen=48)
print("Derived key:", binascii.hexlify(key))

pub,priv=generate_keypair(key)
print(pub.hex())
print(priv.hex())
