import re
str1="something is wrong somewhere"
myreg=re.compile(r"s(.*?)e",re.I)
lst1=myreg.finditer(str1)
for ob in lst1:
    print(ob.group())
    print(ob.group(1))
    print(ob.span())
