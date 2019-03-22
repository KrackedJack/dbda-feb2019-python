def myadd(a,n=10,*d,**args):
	"""this is a doc string that describes the function, 
	assigned to __doc__,used by help()"""
	if a<=0: return 0
	else:
		sum = 0
		for i in range(1,n+1):
			sum = sum + a  
		print("sum")

	return a,n,d,args

x=12
y=34
print(myadd(10,2,56,12,0,"dfg", x=12,y=34,z=56))	