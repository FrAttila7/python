class Kerekpar:
	sebesseg = 0
	

	
	def __init__(self, szin):
		self.sebesseg = 0
		self.szin = szin
	
	def novelSebesseg(self):
		self.sebesseg = self.sebesseg + 1



	def telikIdo(self):
		while True:
			self.novelSebesseg()
			cmd = input("> ")
			if cmd == "vege":
				exit()
				
		
		
		
kerekpar = Kerekpar("piros")
kerekpar.telikIdo()
#kerekpar.novelSebesseg()
#print(kerekpar.szin)
