a=[1,4,6,78,123,2,35]
hossz=len(a)
max=a[0]
for i in range(0, hossz):
	if max<a[i]:
		max=a[i]
print(max)
