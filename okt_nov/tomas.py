a = [35, 75, 49]
b=a[::]
print(a)
print(b)
a[0] = 80
b=a[::-1]
print(a)
print(b)
c = [43, 27]
  
f=a+c
print(f)
a.extend(range(5,10))
print(a)

