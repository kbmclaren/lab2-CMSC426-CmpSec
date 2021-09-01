import time

# New key generation function [3/18/2021]
def genkey(keylen):
        n = 278680767812959796815817796531952571
        x = int(time.time()) & 0xffffff
        key = bytearray(keylen)
        for i in range(keylen):
                key[i] = 0
                for j in range(8):
                        x = (x*x) % n
                        key[i] = (key[i] << 1) ^ (x & 1)
        return(bytes(key))
