import os, sys

class filemodule:
	def __init__(self, src):
		if os.path.exists(src):
			with open(src) as fr:
				flist = fr.readlines()
		else: 
			flist = list()

		appendFlag = modifyFlag = False
		added  = deleted = 0
		lcount = len(flist)
		print(lcount, flist)
