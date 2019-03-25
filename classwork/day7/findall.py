import re
str1="This is something somewhere"
lst= re.findall(r"s.*?e",str1)
print(len(lst))
print(lst)
