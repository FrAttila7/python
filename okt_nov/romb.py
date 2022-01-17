#File: romb.py
#Auth: Frank Attila
#Date: 2021.11.16
#Copyright: 2021, Frank Attila
#Github: https://github.com/FrAttila7
#Licenc: GNU GPL
#Group: Ifra I N

import math

print("Frank Attila")
print("310")
print("Rombusz területének és kerületének kiszámolása")

oldal=int(input("Oldal hossz: "))
szog1=int(input("Szög: "))
rad=szog1*math.pi/180
szog2=math.sin(rad)
magassag=oldal*szog2

kerulet=4*oldal
terulet=oldal*magassag

print("Kerület: ", kerulet)
print("Terület: ", terulet)


