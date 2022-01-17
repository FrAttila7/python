zold_nev = input("Zöldség neve: ")

if zold_nev == "":
	exit()
	
zoldsegek= ["hagyma","karalábé","cékla"]
	
if zold_nev in zoldsegek:
	print("Rendben")
else: 
	print("Nincs ilyen zöldség")
	
