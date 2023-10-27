from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64
import os
import hashlib
from ast import literal_eval
from operator import xor
import subprocess

text = '5361626168204973205468652042657374' # hex
text2 = '41706b616c657373204865206973204972617169204c6567656e64' # hex

integer1 = int(text, 16)
integer2 = int(text2, 16)

binary1 = bin(integer1)[2:]
binary2 = bin(integer2)[2:]

len_bin1 = len(binary1)

len_bin2 = len(binary2)

length = len_bin1 if len_bin1 > len_bin2 else len_bin2

 
eq_length1 = binary1.zfill(length)
eq_length2 = binary2.zfill(length)


result = []

for n1, n2 in zip(eq_length1, eq_length2):

    result.append(xor(int(n1), int(n2)))


final_result = ''.join(str(a) for a in result)


hex_ = hex(int(final_result, 2))[2:]

print(bytes().fromhex(hex_))

