class Dolgozo: 
	def __init__(self):
		self.nev = "névtelen"
		self.telepules = "ismeretlen"
		self.fizetes = 0
		
	def allitNev(self, atvettNev):
		self.nev = atvettNev 
	def kerNev(self):
		return self.nev

class Mernok(Dolgozo):
	def __init__(self):
		self.diploma = "ismeretlen"
		
		
kati = Mernok()
kati.allitNev("Latner Katalin")
kati.diploma = "ABC-1234"
print(kati.diploma)
	
