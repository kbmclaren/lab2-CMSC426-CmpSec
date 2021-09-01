# File: genKeyWTimes.py
# Modified by: Caleb M. McLaren
# Author: ? Dr. Christopohor Marron
# Date: April 6th, 2021
# email: mclaren1@umbc.edu
# Description: this Python function is used to generate keys for the antiZendian.py script

import time

#modified to receive your choice of time
def genKeyWTimes(keylen, thatInstant):
        n = 278680767812959796815817796531952571
        x = int(thatInstant) & 0xffffff
        key = bytearray(keylen)
        for i in range(keylen):
                key[i] = 0
                for j in range(8):
                        x = (x*x) % n
                        key[i] = (key[i] << 1) ^ (x & 1)
        #print(len(key)) # confirm key length
        return(bytes(key))
