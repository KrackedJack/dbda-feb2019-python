import re
str1="something is wrong somewhere"
myreg=re.compile(r"s(.*?)e",re.I)
lst1=myreg.sub("any",str1,count=1)#count here is used for replacing the first occurance only
#re.sub(r"s(.*?)e,"any",str1,flags=0)----> if using re only
#for ob in lst1:
    #print(ob.group())
    #print(ob.group(1))
    #print(ob.span())
