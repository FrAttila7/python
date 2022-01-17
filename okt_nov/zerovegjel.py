#File: zerovegjel.py
#Author: Frank Attila
#Copyright: 2021, Frank Attila
#Group: Ifra I N
#Date: 2021.10.19 
#Github: https://github.com/FrAttila7
#Licenc: GNU GPL

print("Frank Attila, Ifra I N, 2021.10.19")
print("Feladat 0701")
print("Összeadja a bekért számokat 0 végjelig")

szam = -1
osszeg = 0
while szam != 0:
 szam= int(input("Szám: "))
 osszeg = osszeg + szam


print("összeg:", osszeg)
