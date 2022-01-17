


def zoldVizs(zold_nev):
	zoldsegek=["karalábé","vöröshagyma","cékla","paprika"]
	if zold_nev in zoldsegek:
		return True
	else:
		return False

zold_nev = ""
darab_jo = 0
while zold_nev != "vege":
	zold_nev=input("Zöldség neve: ")
	if zold_nev!= "vege":
		if zoldVizs(zold_nev):
			print("Ok")
			darab_jo += 1
		else:
			print("Nem megfelelő zöldség")
print("Jó zöldségek darabszáma: ",darab_jo)
