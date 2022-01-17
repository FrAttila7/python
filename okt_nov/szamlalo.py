dec=[1,3,0,0,5,4,2]
szamlalo=0
hossz=len(dec)
for i in range(0, hossz):
	if dec[i]< 0:
		szamlalo = szamlalo +1
	print(szamlalo)
