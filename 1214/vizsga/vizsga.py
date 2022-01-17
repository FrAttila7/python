#nev=str(input("Add meg a vizsgázó nevét!: "))
#pont=int(input("Add meg a vizsgázó pontszámát!: "))



while True:
	nev = input("Add meg a vizsgázó nevét!: ")
	if nev == "":
		print("Vége")
		break
	pont=int(input("Add meg a vizsgázó pontszámát!: "))
	
	if pont>=48:
		print(nev+" vizsgája sikeres!")
	else:
		print(nev+" vizsgája sikertelen.")
