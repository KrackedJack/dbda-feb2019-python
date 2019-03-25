import matplotlib.pyplot as plt
days=[1,2,3,4,5]
sleeping=[7,5,6,8,9]
eating=[1,3,2,4,2]
working=[9,10,12,7,8]
playing=[0,1,1,2,1]
plt.plot([],[],color='m',label='Sleeping',linewidth=5)
plt.plot([],[],color='c',label='Eating',linewidth=5)
plt.plot([],[],color='r',label='working',linewidth=5)
plt.plot([],[],color='b',label='playing',linewidth=5)
plt.stackplot(days,sleeping,eating,working,playing,colors=['m','c','r','b'])
plt.xlabel('plot number')
plt.ylabel('Important var')
plt.legend(loc="Upper left")
plt.title("First")
plt.show()