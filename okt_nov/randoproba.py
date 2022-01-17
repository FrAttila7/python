import random
numberlist=[ ]
szamlalo= 0
for i in range(0, 500):
	numberRand=random.randrange(1, 501)
	numberlist.append(numberRand)

#print(numberlist)
#print(len(numberlist))

for number in numberlist:
	if numberlist[number] > 250 :
		szamlalo=szamlalo+1
		print(szamlalo)

