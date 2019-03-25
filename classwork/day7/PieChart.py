import matplotlib.pyplot as plt
slices=[1,2,3,4,5]
activities=['a','b','c','d','e']
cols=['g','y','b','k','r']
plt.pie(slices,labels=activities,colors=cols,shadow=True)
plt.show()

