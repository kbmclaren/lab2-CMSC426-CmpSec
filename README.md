# lab2-CMSC426-CmpSec
## Description
In this lab I worked with my group to analyze three encooded messages. Together we determined the encryption algorithm and plaintext formatting of the intercepted messages. We also analyzed an intercepted key generation algorithm and the method used to generate randomness in the key generation algorithm. Using the information gained above, we successfully decrypted the secret messages.<br> 
## Repo Contents
- DecryptHere : This folder conatins the following: original lab files, the modified genKeyWithTimes.py, and the original antiZendian.py<br>
    - antiZendian.py : This original code(author: self) searches across a potential key space and generates files for swift human analsysis. This approach vastly sped up the process involved in determining if the correct encryption key had been used for the decryption.This file requires pycrypto, genKeyWTimes, msg2.enc ,msg3.enc, and metadata.txt<br>
    - genkey.py: key generator provided for analysis.<br>
    - genKeyWTimes: modified genkey.py, takes second variable.<br>
    - metadata.txt: data about the encoded messages.<br>
    - msg*.enc: the encrypted "Zendian" messages provided for analysis.<br>
- "Lab 2-Group 8-CMSC426-Spring2021.pdf": This file is the group document, submitted for grading, in response to document "modern_crypto_lab.pdf"<br>
- README.md<br>
- "decr:1616119054.0.txt" : This file is the first decoded Zendian message.<br>
- "decr:1616119323.0.txt" : This file is the second decoded Zendian message.<br>
- "modern_crpyt_lab.pdf" : This file contains the lab 2 requirements and instructions.<br>