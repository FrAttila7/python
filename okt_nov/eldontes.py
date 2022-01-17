numbers = []

for i in range(0, 5):
	number = int(input("Szám: "))
	numbers.append(number)
	
print(numbers)
find= int(input("Keresett: "))
check = False
for number in numbers:
	if(number==find):
		check = True
if(check):
	print("Van ilyen")
else:
	print("Nincs ilyen")
