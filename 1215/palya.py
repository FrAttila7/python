#Frank Attila 
#2021-12-15
#IFRA

print("Frank Attila")
print("2021-12-15")
print("IFRA")

terulet=["Budapest", "Miskolc", "Zalaegerszeg", "Pécs"]
bekert=input("Kérek egy területet: ")
while bekert in terulet:
	palya=input("Területhez tartozó pálya: ")
	oreg=int(input("Öregedési idő: "))
	if oreg > 5:
		print("Sürgős karbantartás!")
	if oreg <6 and oreg>2:
		print("Felülvizsgálatot igényel")
	else:
		print("Normál")

