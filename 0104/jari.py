from jaro import Jarmu

class Auto:
	def read_file(self):
		fp = open('jari.txt','r',encoding="utf-8")
		lines = fp.readlines()
		fp.close()

		self.jarmuvek = []

		for line in lines[1::]:
			(rendszam, nev, uzemanyag, ev, ar, klima, muszaki) = line.split(':')
			auto = Jarmu(rendszam, nev, uzemanyag, ev, ar, klima, muszaki)
			self.jarmuvek.append(auto)


	 
	 
	def showBenzin(self):
		for auto in self.jarmuvek:
			if auto.uzemanyag=="benzin":
				print("Benzines autók: ",auto.rendszam, auto.nev, auto.ev, auto.ar, auto.klima, auto.muszaki)
				
				
			


	def lessThanMillion(self):
		for auto in self.jarmuvek:
			if auto.ar < 1000000:
				print("Autók olcsóbbak mint 1M: ",auto.rendszam, auto.nev, auto.ev, auto.ar, auto.klima, auto.muszaki)
				
	
	def showHondak(self):
		for auto in self.jarmuvek:
			if auto.nev == "Honda":
				print("Honda: ",auto.rendszam, auto.ev, auto.ar, auto.klima, auto.muszaki)




auto = Auto()
auto.read_file()
auto.showBenzin()
auto.lessThanMillion()
auto.showHondak()
