#!/usr/bin/python3
import pyAesCrypt
import os
# script by : @anir0y for DSCI class!
banner = """
THis script can encrypt data.txt file by default!
"""

print (banner)
# take key as user input
passkey = input("Your Secret key: ")
# encryption/decryption buffer size - 64K
bufferSize = 64 * 1024
password = passkey
# encrypt
pyAesCrypt.encryptFile("data.txt", "data.aes", password, bufferSize)
print ("Encrypted File! check for data.txt.aes")
print ("Password is "+ passkey)
os.system('clear')
#encode to base64 
print ("Processing... data to baase64")
os.system("base64 data.aes -w 0 > dataencoded.txt")
os.system("rm data.aes")
print ("data encryptd and encoded!")
print ("Password is "+ passkey)
print("done!!!") 
