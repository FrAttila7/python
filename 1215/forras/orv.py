#Frank Attila 
#2021-12-15
#IFRA

print("Frank Attila")
print("2021-12-15")
print("IFRA")

from paciens import Paciens

class Orv:
	def __init__(self):
		self.file_name = "paciens.txt"
		self.paciensek = []

	def beolvas(self):
		fp = open(self.file_name,"r",encoding="utf-8")
		sorok = fp.readlines()
		fp.close()
		self.paciensek = []
		for sor in sorok:
			(nev, tunet, kezeles, ido, ar) = sor.split(':')
			paciens = Paciens(nev, tunet, kezeles, ido, ar)
			paciensek.append(paciens)
    
	def moxavalKezeltek(self):
		for paciens in self.paciensek:
			if paciensek.tunet == "moxa":
				print(paciens.nev)
        

	def bevetel(self):
		pass

	def tizezernelNagyobbBevetel(self):
		pass

orv = Orv()
paciens = Paciens()
orv.moxavalKezeltek()
