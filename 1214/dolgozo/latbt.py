from dolgozo import Dolgozo

class Latbt:
	def olvas_fajl(self):
		fp = open("latbt.txt","r",encoding="utf-8")
		lines = fp.readlines()
		fp.close()
        
		self.dolgozok = []
		for line in lines:
			(nev, telepules, fizetes) = line.split(':')
			dolgozo = Dolgozo(nev, telepules, fizetes)
			self.dolgozok.append(dolgozo)
            

	def szamitAtlag(self):
		for dolgozo in self.dolgozok:
			fizetes = int(dolgozo.fizetes)
			darab = len(self.dolgozok)
			osszeg = 0
		osszeg + fizetes
			atlag = osszeg / darab
		return atlag
		print(osszeg)
				
			
			
	def kiirTelepulesek(self):
		talon= []
		
		for dolgozo in self.dolgozok:
			if dolgozo.telepules not in talon:
				print(dolgozo.telepules)
				talon.append(dolgozo.telepules)
				

	
	def bekerDolgozo(self):
		nev = input("Név: ")
		telepules = input("Telepules: ")
		fizetes = input("Fizetés: ")
		dolgozo=Dolgozo(nev, telepules, fizetes)
		self.kiirFajlba(dolgozo)
		
		
		
	def kiirFajlba(self, dolgozo):
		fp = open('uj.txt',"w",encoding="utf-8")
		fp.write(dolgozo.nev)
		fp.write(':')
		fp.write(dolgozo.telepules)
		fp.write(':')
		fp.write(dolgozo.fizetes)
		fp.write('/n')
		fp.close()


latbt = Latbt()
latbt.olvas_fajl()
latbt.szamitAtlag()
latbt.kiirTelepulesek()
latbt.bekerDolgozo()
