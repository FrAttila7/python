# File: maganhangzo.py
# Author: Frank Attila
# Copyright: 2021,Frank Attila
# Group: IFRA 1N
# Date: 2021-11-30
# Github: https://github.com/frattila77/
# Licenc: GNU GPL

print("Frannk Attila IFRA 1N")
print("1056-es feladat")
print("Megszámolja bekért karakterek magánhangzóit")

karlanc=input("Karakterlánc: ")
magan=['a','á','e','é','i','í','o','ó','ö','ő','u','ú','ü','ű']
darab=0
for kar in karlanc:
	if kar in magan:
		darab+=1
		
print("Magánhangzók száma: ",darab)
