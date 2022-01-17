# File: fuggdup.py
# Author: Frank Attila
# Copyright: 2021,Frank Attila
# Group: IFRA IN
# Date: 2021-11-30
# Github: https://github.com/frattila77/
# Licenc: GNU GPL


#ASCII táblában 97-122 az abc betúi
#print(chr(97))
#print(chr(122))

import random

vel=random.randrange(97, 123)


print(chr(vel))


list=[]

#függvény

def feltoltbetu(list):
	for i in range(0,100):
		vel=random.randrange(97, 123)
		list.append(chr(vel))

	
betulista=[]
feltoltbetu(betulista)
print(betulista)
