# File: antiZendian.py
# Author: Caleb M. McLaren
# Date: April 6th, 2021
# email: mclaren1@umbc.edu
# Description: this Python script must implement an attack on the encrypted files 
#   provided in lab 2 of CMSC 426, Spring 2021, at UMBC, Dr. Christophor Marron presiding.

# Requirements: 
    # pycrpyto (pip install pycrypto)
    # genKeyWTimes.py
    # msg2.enc & msg3.enc
    # metadata.txt

# References:
    # https://docs.python.org/3/library/time.html#time.struct_time
    # https://youtu.be/UB2VX4vNUa0
    # https://github.com/the-javapocalypse/Python-File-Encryptor/blob/master/script.py
    # https://www.dlitz.net/software/pycrypto/api/current/
    #

import time as t
from genkey import genkey
from genKeyWTimes import genKeyWTimes
from Crypto.Cipher import AES

# DAY = 3/18/2021
# REF1 = 21:57
# REF2 = 22:02

# mssg2TimeStamp = (2021, 3, 18, 21, 57)
# mssg3TimeStamp = (2021, 3, 18, 22, 2)

# year, month, day, hour, minute, second, day of the week, day count of the year, daylight savings time
# see https://docs.python.org/3/library/time.html#time.struct_time
startTime = (2021, 3, 18, 21, 56, 0, 3, 77, 1)

#initilize timestamp list
listMssgCreationTimestamps = [ ] 
x = startTime[3]
y = startTime[4]
z = startTime[5]
while x < 22 :
    while y < 63 :
        while z < 60:
            if (y >= 60) :
                x = 22
                y = y - 60  
                newTimeStamp = (2021, 3, 18, x, y, z, 3, 77, 1)
                listMssgCreationTimestamps.append( newTimeStamp )
                y = y + 60 
            else:
                newTimeStamp = (2021, 3, 18, x, y, z, 3, 77, 1) 
                listMssgCreationTimestamps.append( newTimeStamp )   
            z += 1
        y += 1
        z = 0 
    x += 1

# great got our list of timestamps.
#print(listMssgCreationTimestamps) 

listOfFloats = []
for i in range(len(listMssgCreationTimestamps)) :
    #mktime was chosen to convert from local time to seconds since epoch.
    whatIsThisFloat = t.mktime( listMssgCreationTimestamps[i] )
    listOfFloats.append( whatIsThisFloat )

# we have a list of times to replace the returns of time.time() in the genkey.py
#print(listOfFloats) 

# write times to file
with open("timesForGenkey.txt", "w") as writer:
    for minute in listOfFloats:
        writer.write(str(minute) + ",\n")
writer.close()

# using list of times to generate keys for those minutes
dictOfKeys = {} 
for sec in listOfFloats:
    newKey = genKeyWTimes(16, sec)
    dictOfKeys[sec] = newKey

# write keys to file for visual comparison
# write keys as strings to .txt file
with open("keysFromTimes2.txt", "w") as writer:
    for i in dictOfKeys:
        writer.write(str(i) + ": " + str(dictOfKeys[i]) + "\n")
 

# Now to use the AES algorithm in codebook mode with our keys to decrpyt the messages. 
listOfPlainTxt = []
#listOfMssf = ["msg2.enc"]
listOfMssg = ["msg3.enc"]
#listOfMssg = ["msg2.enc", "msg3.enc"]

for mssg in listOfMssg:
    with open(mssg, 'rb') as fo:
        cipherText = fo.read()
        for key in dictOfKeys:
            iv = cipherText[:AES.block_size]
            obj = AES.new( dictOfKeys[key], AES.MODE_ECB, iv)
            plainTxt = obj.decrypt(cipherText[AES.block_size:])

            #If key found, plaintext will be obvious in the file preview window of a Mac file system.
            # for every novel key, generate a novel file to hold the potentially decrypted text. 
            filename = "decr:" + str(key) +".txt"
            f = open(filename, "wb")
            f.write(plainTxt)
 
fo.close()
f.close()


