from adat import Adatok
from typing import List

class Lentbt:
	def olvas_fajl(self):
		fp = open("lentbt.txt","r",encoding="utf-8")
		lines = fp.readlines()
		fp.close()
        
		self.lent = []
		for line in lines:
			(id, nev, telepules, cim, fizetes, szul) = line.split(':')
			lent = Adatok(id, nev, telepules, cim, fizetes, szul)
			self.lent.append(lent)
	
	def more_Than_2million(self):
		osszeg = 0
		for lent in self.lent:
			if lent.fizetes > 2000000:
				osszeg+=1
		print(osszeg)
		
		
lent = Lentbt()
lent.olvas_fajl()
lent.more_Than_2million()
