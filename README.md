Secure Communitcations – RSA LABS 
https://en.wikipedia.org/wiki/RSA_(cryptosystem)

RSA:-
RSA (Rivest-Shamir-Adleman) is one of the first public key cryptosystems and is known world widely for being used for secure data transmission. In such a cryptosystem, the encryption key is public and it is different from the decryption key which is kept secret.
RSA Challenge 1 : 
In the first challenge I was given the values of the 4 letters p,q,e,n and d. I must use the string given to me “RSA isn’t really that hard” for conversation. 
 First import the binascii, which is the conversion between binary and ASCII. It contains several methods. Then use the string2int option to convert the string to a byte and the string2string option to convert a int to a string. You will use the binascii.hexlify function. Which returns the hexadecimal representation of the binary data. Every byte of data is converted into the corresponding 2-digit hex representation. The resulting string is therefore twice if the length of date. Than the binascii.unhexlify function which returns the binary data represented by the hexadecimal string hexstr. This function is the inverse of b2a_hex(). hexstr must contain an even number of hexadecimal digits (which can be upper or lower case), otherwise a TypeError is raised. 
Then for then encryption you would use (pow) method to do the encryption. The pow() method returns the x to the power of the y.  You then can choose a letter or a word to represent the plain text message you have. I used the letter H.  Than next is to decrypt it. Converting the number gotten into a string value. 
The results are: 
ZD{13309476856206179288137278795001286676504235122200291222905951541015281640474228799375180129564959032261555135231635439690367282451635413048574322588643043250005501837597608399627442074603517951858976430767446724730937928672932493206869274420288717036712376949408229648116702610597844919828482630797157003777363091998366855062763360538948110895070725322039940644906900772757193759215740687066380017485804644723367158972689710477927318380335919282326398046586751715463059075476044138690978986063001880735783893361380726584661054926968590764176030209214513123458853087059980258593405395678238799024217478961749328706800}
RSA isn't really that hard

RSA Challenge 2 : 
In this challenge I am asked to decrypt a cipher text value using the exact same values I was given from level one. This meant to me that the two levels were the same except one was encryption and the other was decryption. 
The one extra bit is adding the cipher text value into the code labeled ciphertext to be clear in mine. 
The results are: 
ZD{Well Done you have decrypted correctly} 

RSA Challenge 3 : 
In this challenge we are asked to find out the value of n,e and d by giving us a RSA private key. 
Private key is sued for authentication and a symmetric key exchange during establishment of an SSL/TLS session. The private key has all the elements.
After reading more about RSA I came across a method called (Crypto.PublicKey.RSA) .
This method provides the key for generating new RSA keys and reconstructing them from the known components, exporting them out and importing them in. Just what we wanted. From the ( from Crypto.PublicKey import RSA ) we will import RSA which will help them read through the private key to solve the puzzle. 
I also imported the file ‘mykey2’ which has the RSA private key on it, using the RSA.importKey with the direct path to the file. 
Then I done a print statement with the key.() and the letter to achieve the values of them. 
The results are: 
ZD{25804750360904248224329381618104859031736073222395248860499133051128513648896523325052435992237099000924849024564826844234697029915822571039994777064514824635243492963301478168480948385273501322600327794162141312212647635059765199895820389754402745012084674140342116327728380193544092902468871988407101113210818201750378837933282937750636399588218292079918162950294282004250547116764896324653457065316101365613347914317959505469586731762453963212022535424803572822031093301253062385003468990260150084465026582297271243286096414015105084255301102689693963566336024015793743350044649378818363190804537712326729609503119, 65537, 25564173244610971210351548452585197331194535758994673657884351015114666175874020376311922413781312689534869581593541780807512387877301314484073132668426835287971970400465565582293880630212968962130535153634911375813942663745522611172864711921423815900248860235223648392420965446176110834882493594752879241898541637225074107295433979711279703743206408857411263301020537809364614125840424406332180800207630227259634428188684178985515460114123914453650465520564263249152086786817100938246123146166512963816583276055667323176816331368813221646162976565638562106256552057858358804329568634212548081342870432443412497223185}

RSA Challenge 4 :
This challenge wanted me to decrypt a cipher text using RSA private key. This was a mixture of the challenges 2 and 3 into one. I was given a cipher text value and I was given a RSA private key to use.  I accomplished this challenge using the exact code from challenge 2 and 3 put into one. Just the cipher text value was changed along with the RSA private key was changed. 
The results are:
ZD{OK time to move onto some harder stuff}

RSA Challenge 5 :
In this challenge I had to decrypt another cipher text. I was given a file to use with some values.
Using the https://en.wikipedia.org/wiki/RSA_(cryptosystem) website. I wa sable to learn about RSA and the Chinese remainder algorithm. Which is how I solved this flag. Using the solution below. 
# https://en.wikipedia.org/wiki/RSA_(cryptosystem)
#p and {\displaystyle q} q: the primes from the key generation,
#{\displaystyle d_{P}=d{\pmod {p-1}}} {\displaystyle d_{P}=d{\pmod {p-1}}},
#{\displaystyle d_{Q}=d{\pmod {q-1}}} {\displaystyle d_{Q}=d{\pmod {q-1}}} and
#{\displaystyle q_{\text{inv}}=q^{-1}{\pmod {p}}} {\displaystyle q_{\text{inv}}=q^{-1}{\pmod {p}}}.
#These values allow the recipient to compute the exponentiation m = cd (mod pq) more efficiently as follows:

#{\displaystyle m_{1}=c^{d_{P}}{\pmod {p}}} {\displaystyle m_{1}=c^{d_{P}}{\pmod {p}}}
#{\displaystyle m_{2}=c^{d_{Q}}{\pmod {q}}} {\displaystyle m_{2}=c^{d_{Q}}{\pmod {q}}}
#{\displaystyle h=q_{\text{inv}}(m_{1}-m_{2}){\pmod {p}}} {\displaystyle h=q_{\text{inv}}(m_{1}-m_{2}){\pmod {p}}} (if {\displaystyle m_{1}<m_{2}} m_{1}<m_{2} then some libraries compute h as {\displaystyle q_{\text{inv}}\left[\left(m_{1}+\left\lceil {\frac {q}{p}}\right\rceil p\right)-m_{2}\right]{\pmod {p}}} {\displaystyle q_{\text{inv}}\left[\left(m_{1}+\left\lceil {\frac {q}{p}}\right\rceil p\right)-m_{2}\right]{\pmod {p}}})
#{\displaystyle m=m_{2}+hq\,} m=m_{2}+hq\,

#this helps break the decrpytion into 2 pieces
m1 = pow(ciphertext, dp, p)
m2 = pow(ciphertext, dq, q)

#calculates h for us
h = (qinv * (m1- m2)) % p

#reconstracted using the below
decrypted = m2 + h * q

The results are: 
ZD{Those extra private key values are meant to make it easier?}
	
RSA Challenge 6 :
In this challenge I am given a cipher text to decrypt and the values for e,p and q but there is no d value. Which is the main task of this challenge, we must find the value for d. 
After researching about RSA online I came across the method of modular multiplicative inverse python . Once googling it enough times I came across the website https://rosettacode.org/wiki/Modular_inverse#Python  which was the key. 
It gave me a made-out solution to implement with my skills. 
The results are: 
ZD{You are doing very well, you must be starting to understand RSA by now!}
