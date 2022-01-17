# File: bes.py
# Author: Frank Attila
# Copyright: 2021,Frank Attila
# Group: IFRA IN
# Date: 2021-12-07
# Github: https://github.com/frattila77/
# Licenc: GNU GPL

print("Frannk Attila IFRA IN")
print("1055-es feladat")
print("Bekért karakterlánc hány b-t tartalmaz")

karlanc=input("Karakterlánc: ")
bbetu=["B","b"]
darab=0
for kar in karlanc:
	if kar in bbetu:
		darab+=1
		
print("b betűk száma: ",darab)
