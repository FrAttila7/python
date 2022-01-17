#Frank Attila
#2021.01.10.
#IFRA I N

from country import Country
from typing import List

class Mikronezia:
	def __init__(self):
		self.countries:List[Country] = []
		self.sep = ':'
		
	def read_content(self):
		file_name = 'countries.txt'
		fp = open(file_name, 'r', encoding="utf-8")
		self.lines = fp.readlines()
		fp.close()

	def convert_content(self):
		for line in self.lines[1::]:            
			(id, name, area, population) = line.split('#')
			country = Country(id, name, int(area), int(population))
			self.countries.append(country)

	# Legnépesebb ország
	def most_populated(self):
		max_country = self.countries[0]
		for country in self.countries:
			if country.population > max_country.population:
				max_country = country
		print("Legnépesebb ország: ", max_country.name,"|", max_country.population)

	# Legkisebb területű ország
	def smallest_area(self):
		min_country = self.countries[0]
		for country in self.countries:
			if country.area < min_country.area:
				min_country = country
		print("Legkisebb ország: ", min_country.id , "|",min_country.name,"|", min_country.area,"|", min_country.population)

	# 99 ezernél kisebb népesség
	def less_than_ninety_nine_thousand(self):
		keves = 99000
		for country in self.countries:
			if country.population < keves:
				print("99ezernél kisebb lakosságú országok : " , country.name,"|", country.population)

	# Hány 500 négyeztkilométernél nagyobb területi ország van?
	def more_than_five_hunderd_area(self):
		szamlalo = 0
		nagy = 500
		for country in self.countries:
			if country.area > nagy:
				szamlalo += 1
		print("500 négyzetkilóméternél nagyobb országok száma: ", szamlalo)

	# Hány ország nevében szerepel a "sziget" szó?
	def island_word_in_name(self):
		szamlalo = 0
		for country in self.countries:
			if country.name.find("sziget") != -1:
				szamlalo +=1 
		print("A sziget szót ennyi ország nevében szerepel: ", szamlalo)
		
	# Az országok területe összesen
	def sum_areas(self):
		osszeg = 0 
		for country in self.countries:
			osszeg = osszeg + country.area
		print("Országok össz területe: ",osszeg,"Km2")
			

	# Az országok népességének átlaga
	def population_average(self):
		oszto = 0
		osszeg = 0
		for country in self.countries:
			oszto += 1
			osszeg = osszeg + country.population
		atlag = osszeg / oszto
		print("Országok népességének átlaga: %.2f" % atlag)

	# Állapítsuk meg, hogy egyszavas, vagy nem, a név
	def is_one_word(self, country):
		for country in self.countries:
			if country.name.find("-") == -1:
				return True
			else:
				return False

	def write_a_country(self, fp, country):
		fp.write(country.id)
		fp.write(self.sep)
		fp.write(country.name)
		fp.write(self.sep)
		fp.write(str(country.area))
		fp.write(self.sep)
		fp.write(str(country.population))
		fp.write('\n')


	def write_one_word(self):
		fp = open('oneword.txt', 'w', encoding = "utf-8")
		for country in self.countries:
			if self.is_one_word(country):
				self.write_a_country(fp, country)
		fp.close()


mikro = Mikronezia()
mikro.read_content()
mikro.convert_content()
mikro.most_populated()
mikro.smallest_area()
mikro.less_than_ninety_nine_thousand()
mikro.more_than_five_hunderd_area()
mikro.sum_areas()
mikro.island_word_in_name()
mikro.population_average()
mikro.write_one_word()


