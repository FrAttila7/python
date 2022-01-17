import random
import math
numbers1=[]
numbers2=[]
for i in range(0, 5000):
	numberRand=random.randrange(1, 101 )
	numbers1.append(numberRand)
	
print(len(numbers1))
print(numbers1[6])

for number in numbers1:
	powered= math.pow(number, 3)
	numbers2.append(powered)

print(numbers2[6])

numbers1sum=0
numbers2sum=0
for number in numbers1:
	numbers1sum+=number

for number in numbers2:
	numbers2sum+=number
	

print("1. lista összeg", numbers1sum)
print("1. lista összeg", numbers2sum)
	
