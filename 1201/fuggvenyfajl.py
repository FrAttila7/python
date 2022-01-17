"""
dolgozók megszámlálása
miskolci dolgozók fizetés összege
van-e Lajos nevű dolgozó?
"""

def countWorker():
	
	file = open('feherBt.txt' , "r", encoding="utf-8")
	row = file.readline()
	counter = 0
	while( row ):
		
		row = file.readline()
		if( len(row) > 0 ):
			counter+=1
	
	print("A dolgozók száma: ", counter)
	file.close()
	
	
def sumMiskolc():
	file = open('feherBt.txt' , "r", encoding="utf-8")
	row = file.readline()
	miskolcSalary = 0
	while ( row ):
		row=file.readline()
		if(len(row)>0):
			
			rowSpt= row.split( ":" )
			if(rowSpt[1]=="Miskolc" ):
				
				miskolcSalary+= int(rowSpt[ 3 ])
				
	print("Miskolciak fizetése: ", miskolcSalary)
	file.close()
			

def countLajos():
	file = open('feherBt.txt' , "r", encoding="utf-8")
	row = file.readline()
	sumLajos=0
	
	while(row):
		row=file.readline()
		if( len(row)>0 ):
			rowSpt=row.split(":")
			nameSpt=rowSpt[0].split(" ")
			if(nameSpt[1]=="Lajos"):
				sumLajos+=1
	if(sumLajos > 0):
		print("Lajosok száma: ", sumLajos)
	else:
		print("Nincs ilyen név")
	file.close()



		
def start():
	countWorker()
	sumMiskolc()
	countLajos()

start()


