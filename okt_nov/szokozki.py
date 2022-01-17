#File: beljebb.py
#Author: Frank Attila
# Copyright: 2021, Frank Attila
#Group: 13.IFRA
#Date: 2021-11-15
#Github: https://github.com/Fr.Attila77
print("Frank Attila")
print("2021-11-15")
print("Kérjen be egy mondatot, majd szedje ki a szóközöket, ha abból egynél több van benne.")
print("1069-es feladat")

szam=0
mondat="      Szia uram       "
print(mondat)
for i in mondat:
    if(i.isspace()):
        szam=szam+1
print("Szóközök száma: ",szam)
if szam>=2:
	mondat.strip(" ")
	print(mondat)
else:
    print("Kevesebb mint 2 space van benne")

