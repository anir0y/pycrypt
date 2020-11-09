#!/usr/bin/python3
import pyAesCrypt
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
pyAesCrypt.encryptFile("data.txt", "data.txt.aes", password, bufferSize)
print ("Encrypted File! check for data.txt.aes")
print ("Password is "+ passkey)

