import os
if os.path.exists("empdata.txt"):
    with open("empdata.txt") as fh:
        flist=fh.readlines()
else:
    flist= []
ans='y'
while ans=='y':
    eno=int(input("Please enter the Emp no: "))
    varen=input("Please enter the Emp name: ")
    varsal=int(input("Please enter the Emp salary: "))
    vardesig=input("Please enter the Emp designation: ")
    flist.append(str(eno)+":"+varen+":"+str(varsal)+":"+vardesig)
    print(flist)
    with open("empdata.txt","w")as fa:
        for f in flist:
            fa.write(f+"\n")
    ans=input("Do you want to continue(y/n)")

