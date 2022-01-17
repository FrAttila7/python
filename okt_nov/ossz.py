a= [1,2,3,4,5,6,7,8]
hossz=len(a)
osszeg=0
for i in range(0, hossz):
	#print(a[i], end=' ')
	osszeg = osszeg + a[i]
print("Összeg: ", osszeg)
