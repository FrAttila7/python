#Frank Attila 
#2022-01-03
#IFRA

print("Frank Attila, 2022.01.03")
print("Híd típusának bekérése")

tipus=input("Híd típus: ")

if tipus == "":
	exit()
	
hid=["gerenda","Gerenda","keret","Keret","konzolos","Konzolos"]

if tipus in hid:
	print("Hajlító vagy nyíró igénybevételek alapján tipizált.")
else:
	print("Ismeretlen típus.")
	
