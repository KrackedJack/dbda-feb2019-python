import functools as ft
lst = [10,25,3,45,35,20,1]

print(list(map(lambda x:x+20,lst)))
print(list(filter(lambda x:x>20,lst)))

lst = [(4,"four"), (5,"six"),(10,"Ten") ]
lst.sort(key=(lambda x:x[1]))
print(lst)

lst = [10,25,3,45,35,20,1]
print(ft.reduce(lambda x,y:x if x<y else y,lst))