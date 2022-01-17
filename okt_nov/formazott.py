name = "Joe"
age = 43

result =  "Név: %s Kor: %d" 
print( result % (name , age))

res = "Név: {name} Kor: {age}"
print( res.format( name="Joe", age= 43) )
