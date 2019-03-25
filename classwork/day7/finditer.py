import re
str1="This is something serious somewhere"
lst=re.finditer(r"s(.*?)e",str1)
for ob in lst:
    print(ob.group())
    print(ob.group(1))
    print(ob.span())
