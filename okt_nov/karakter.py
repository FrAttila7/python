#File: karakter.py
#Author: Frank Attila
#Copyright: 2021, Frank Attila
#Group: Ifra I N
#Date: 2021.10.19 
#Github: https://github.com/FrAttila7
#Licenc: GNU GPL

print("Frank Attila, Ifra I N, 2021.10.19")
print("Karakter")

print(chr(97))
print(chr(98))
print(chr(99))

# angol abc kis betűi

szamlalo=1
for i in range (97, 123):
	print (chr(i), end=' ')
	if szamlalo % 5==0:
		print('\n')
	szamlalo += 1 
