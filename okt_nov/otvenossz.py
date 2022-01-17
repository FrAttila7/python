#File: otvenossz.py
#Auth: Frank Attila
#Date: 2021.11.16
#Copyright: 2021, Frank Attila
#Github: https://github.com/FrAttila7
#Licenc: GNU GPL
#Group: Ifra I N

print("Frank Attila")
print("730")
print("Bekéri a számokat 0 végjelig, miközben összegezi azokat, ha azok nagyobbak mint 49. Ha szám 49 vagy kisebb, akkor hibaüzenet ír ki.")

szam = -1
osszeg = 0
while szam != 0:
	szam= int(input("Szám: "))
	if szam<=49:
		print("HIBA!")
		print("Összeg: ", osszeg)
	else:
		osszeg+szam
		osszeg=osszeg+szam
		print("Összeg: ", osszeg)
