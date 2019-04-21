#grab cryptokey first
#then use it to import RSA
from Crypto.PublicKey import RSA

key = RSA.importKey(open("mykey2").read()) #reading the rsa private key file


#print the letters you want to find from the private key
print(" ")
print(key.n)
print(" ") #spacing in between for clarity
print(key.e)
print(" ")
print(key.d)




