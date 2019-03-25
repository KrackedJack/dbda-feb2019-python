favColors = {'Arham':'Blue', 'Vinod':'Purple', 'Lisa':'Yellow', 'Jenny':'Pink'}
print(favColors)
print("No. of Students:", len(favColors))
favColors['Lisa'] = 'Red'
print("Lisa's favorite color is now", favColors['Lisa'])
print("Removed", favColors.pop('Jenny'))
lst = []
for i in favColors.keys(): lst.append(i)
lst.sort()
for i in lst:
	print("{}: {}".format(i,favColors[i]))
