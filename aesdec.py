#!/usr/bin/python3 
import pyAesCrypt
#scripted by: @anir0y for DSCI classroom 
banner = """
This will take data.txt.aes as input and decrypt the msg!


"""
print (banner)
# encryption/decryption buffer size - 64K
bufferSize = 64 * 1024
password = input("Aes KEY please: ")
# decrypt
pyAesCrypt.decryptFile("data.txt.aes", "dataout.txt", password, bufferSize)
print ("Data decrypted sucessfully! lookout for dataout.txt")
