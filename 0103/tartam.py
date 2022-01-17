#Frank Attila 
#2022-01-03
#IFRA

print("Frank Attila, 2022.01.03")
print("Híd élettartamának vizsgálata")

def eletVizs(elet_tartam):
	if elet_tartam >=50:
		return "Állandó"
	else:
		return "Rövid"


elet_tartam=-1
while elet_tartam !=0:
	elet_tartam=int(input("Híd élettartama: "))
	if elet_tartam !=0:
		print(eletVizs(elet_tartam))
