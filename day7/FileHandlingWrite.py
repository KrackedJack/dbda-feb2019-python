import os
fa = open("empdata.txt","a")

ans='y'
while ans=='y':
    eno=int(input("Please enter the Emp no: "))
    varen=input("Please enter the Emp name: ")
    varsal=int(input("Please enter the Emp salary: "))
    vardesig=input("Please enter the Emp designation: ")
    fa.write(str(eno)+":"+varen+":"+str(varsal)+":"+vardesig+"\n")
    ans=input("Do you want to continue(y/n)")

fa.close()
# with open("empdata.txt","a") as fa:
#         for f in flist[lcount:]:
#             fa.write(f+"\n")