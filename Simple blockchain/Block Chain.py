import hashlib

#this is the hash value which has been given to us
hash_given = "c89aa2ffb9edcc6604005196b5f0e0e4"

#this is the seed which is given to us that starts the chain up
seed= "ecsc"

#list which will have the hashes in it
list = []

#this will hash the seed , it makes the fish hash in the chain
hashing = hashlib.md5(b"ecsc").hexdigest()

print(hashing)

#now create a while loop
while hashing != hash_given:

#calculating the next hash
# #value_seed = hashlib.md5(hashing.encode()).hexdigest()
#print(value_seed)
#print(hashing)

#hashes the seeds agaun
hashing = hashlib.md5(hashing.encode()).hexdigest()
#appends new values into the list of the hashes
list.append(hashing)
#checking
if(hashing == hash_given):
print("Last hash in the list is: " + hashing)
print("The hash before last hash in list: " + list[-])
