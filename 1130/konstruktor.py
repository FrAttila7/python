class Tama:
	def __init__(self):
		self.nev = "Névtelen"
		self.kor = 0
		self.eletero = 20
	def allitEletero(self, eletero):
		self.eletero = eletero
		
pad= Tama()

adat=''
while adat != "vege":
	adat=input("Adatot kérek> ")
	pad.allitEletero(pad.eletero-1)
	#print(pad.eletero)
	
	if adat == "etet":
		pad.allitEletero(pad.eletero + 10)
		
	if pad.eletero < 5:
		print("Aggyá enni!!!!!!!")
	
	if pad.eletero < 1:
		print(" Meghaltam :( ")
		quit()
