def isPrime(n):
	for i in range(2,int(n/2)):
		if n%i==0:
			return False
			break
	else: return True

print("prime" if isPrime(int(input("Enter number"))) else "not prime")