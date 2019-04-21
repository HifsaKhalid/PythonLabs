SIMPLE BLOCK CHAIN 

The following was my view for this lab task;

Scenario:
You've registered for an online service that uses hash chains.
You've registered as user 'nOOB’ and have been given the hash chain
seed 654e1c2ac6312d8c6441282f155c8ce9
Use the given information to figure out how to authenticate as the user
'ECSC' for the given challenge hash c89aa2ffb9edcc6604005196b5f0e0e4
i.e. Find the hash that hashes to this - This hash will be your solution.

A hash chain is the successive application of a cryptographic hash function to a piece of data.
In computer security, a hash chain is a method to produce many one-time keys from a single key or password. 
The hashes value will be hashed constant amount of times which forms a chain. 

What is the seed value? 
A random seed (or seed state, or just seed) is a number (or vector) used to initialize a pseudorandom number generator.  

We need to find the seed for the given hash value of the user thats given to us and we want to authenciate it. Need to figure out
how the seed was geneated in the first place. 

What was done was that:
We took  list, had the hashes put into a list with a while loop running which compares the seed hashed is the value which is compared to 
with others in more hashes and the correct one is given back. If it doesnt match the last one in the list then it goes again till it does,

The code i done was in two ways. Both ways didnt work out to give the correct hashed value back, one kept running and when stopped never displayed
the correct value. 
The second one after the while loop was probably added with a list in it still didnt work out. 

So i guess this is a uncompleted lab currently. 
