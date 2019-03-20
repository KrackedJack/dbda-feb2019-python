import os
if os.path.exists("read.txt"):
	with open("read.txt") as fhr:
		with open("write.txt","w") as fhw:
			lno=1
			for ln in fhr:
				fhw.write(str(lno) +": "+ln)
				lno = lno + 1
else: print("file not f0wnd") 