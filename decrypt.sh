#!/bin/bash 

echo pass the args

cat  $1 | base64 -d > data.txt.aes 
echo " decryption"
python3 aesdec.py 


echo printing dataout.txt
echo 
cat dataout.txt
echo 
echo 
sleep 3 
echo Deleting all plaintext output for privacy!
rm dataout.txt data.txt.aes 
sleep 2 
clear 

