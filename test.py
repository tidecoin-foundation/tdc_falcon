from tdc_falcon import generate_keypair
import os
import binascii
import hashlib



salt = bytes.fromhex('aaef2d3f4d77ac66e9c5a6c3d8f921d1')
passwd = "Master Key".encode("utf8")

key = hashlib.pbkdf2_hmac('sha512', passwd, salt, iterations=500000, dklen=48)
print("Derived key:", binascii.hexlify(key))

pub,priv=generate_keypair(b'\xae\x101\xe7Xj[Xq\xa5\xaa\x18\x82L\x9dP\x10\x18\xfc\xd7Y\xe8`FO\xa8\x14\x18\xfc\x15\xf1n6?C\xc7\x86\xe5\x99NA\xdf\xf0N\xa7\xfd\xf0\xf3')
print(pub.hex())
print(priv.hex())
