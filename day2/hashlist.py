def bins(d, lst):
	bin = int(str(d)[-1]) 
	if bin<len(lst): lst[bin].append(d)
	else:
		for i in range(len(lst),bin+1):
			lst.append([])
		lst[bin].append(d)
	
lst = list()

bins(10, lst)
bins(12, lst)
bins(13, lst)
#bins(15, lst)
#bins(17, lst)
bins(18, lst)
bins(19, lst)
bins(20, lst)
bins(21, lst)

print(lst)