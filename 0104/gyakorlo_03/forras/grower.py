from product import Product

class Grower:
	def read_file(self):
		fp = open('products.txt','r',encoding="utf-8")
		lines = fp.readlines()
		fp.close()

		self.products = []

		for line in lines[1::]:
			(id, name, price, quantity) = line.split(';')
			product = Product(id, name, price, quantity)
			self.products.append(product)
    
    # legdrágább zöldség
	def larger(self):
		max_product = self.products[0]
		for product in self.products:
			if product.price > max_product.price:
				max_product = product
		print("Legdrágább: ", max_product.name,max_product.price)
    
    # Az összes paprika ára
	def calcPepperPrice(self):
		osszes_ar=0;
		for product in self.products:
			if product.name == "paprika":
				osszes_ar = product.price * product.quantity
		print("Paprika készleten ár alapján: ",osszes_ar)
				
			
			
    # Mennyi a vöröshagyma és a karalábé tömege együtt?
	def sumOnionKohlrabiWeight(self):
		osszegzes = 0
		for product in self.products:
			if (product.name == "karalábé" or 
			product.name == "vöröshagyma"):
				osszegzes += product.quantity
		print("Karalábé és Vöröshagyma összege: ",osszegzes)
    
    # Mi a neve legnagyobb tömegű zöldségnek?
	def showLargerWeight(self):
		max_product = self.products[0]
		for product in self.products:
			if product.quantity > max_product.quantity:
				max_product = product
		print("A legnagyobb tömegű zöldség: ", max_product.name)
    
    # Van karalábé?
	def isHaveKohlrabi(self):
		n = len(self.products)
		ker = "karalábé"
		i = 0
		while i<n and self.products[i].name != ker:
			i+=1
		if i<n:
			print("Van karalábé")
		else:
			print("Nincs")
	

    # Hány zöldség drágább mint 700 Ft.
	def moreThenSevenhundred(self):
		nagy = 0
		for product in self.products:
			if product.price > 700:
				nagy += 1
		print("Nagyobb mint 700: ",nagy,"db")
        

grower = Grower()
grower.read_file()
grower.larger()
grower.calcPepperPrice()
grower.sumOnionKohlrabiWeight()
grower.showLargerWeight()
grower.isHaveKohlrabi()
grower.moreThenSevenhundred()
