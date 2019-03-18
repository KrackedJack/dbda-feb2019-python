alpha = "abcdefghijklmnopqrstuvwxyz"
keys = dict()

def initKeys(n):
	for i,a in enumerate(alpha):
		keys[a] = alpha[(i+n)%26]

def encrypt(s):
	enc=""
	for i in s:
		enc = enc + keys[i]
	return enc	

def decrypt(s):
	dec=""
	for i in s:
		for k,v in keys.items():
			if(v==i):
				dec = dec + k
	return dec


initKeys(13)
print(keys)

print(encrypt(input().replace(" ","").lower()))
print(decrypt(input().replace(" ","").lower()))