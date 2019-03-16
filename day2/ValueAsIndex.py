lst = [12,1,5,7,8,2,8,6]
lst1 = []

for i in range(0,max(lst)+1):
	lst1.append(-1)

print( lst )

count=0
for i in lst:
	print("[{}] = {}".format(i,count))
	lst1[i] = count
	count = count + 1

print( lst1 )
	