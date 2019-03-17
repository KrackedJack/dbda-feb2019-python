def bins(d, lst):
	lst[int(str(d)[-1])].append(d)
	
lst = []
for i in range(0,10):lst.append([])

bins(10, lst)
bins(12, lst)
bins(13, lst)
bins(14, lst)
bins(15, lst)
bins(17, lst)
bins(18, lst)
bins(19, lst)
bins(20, lst)
bins(21, lst)

print(lst)