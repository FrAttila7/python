# File: ketnagy.py
# Author: Frank Attila
# Copyright: 2021,Frank Attila
# Group: IFRA IN
# Date: 2021-11-30
# Github: https://github.com/frattila77/
# Licenc: GNU GPL

print("Frannk Attila IFRA IN")
print("1052-es feladat")
print("Kiírja a hosszabb karakterláncot")

karlanc1=input("Első karakterlánc: ")
karlanc2=input("Második karakterlánc: ")

hossz1=len(karlanc1)
hossz2=len(karlanc2)

if hossz1 > hossz2:
	print("Első karlanc hosszabb, darabszáma: ",hossz1)
	
if hossz1 < hossz2:
	print("Második karlanc hosszabb, darabszáma: ",hossz2)

if hossz1 == hossz2:
	print("Egyforma hosszúak")
