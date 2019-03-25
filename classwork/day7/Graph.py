# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
x=[1,2,3]
y=[5,9,15]
x2=[5,7,9]
y2=[2,3,8]
plt.plot(x,y,label="First Line")
plt.plot(x2,y2,label="second Line")
plt.xlabel("aplot number")
plt.ylabel("important var")
plt.legend()
plt.grid()
plt.title("graph diagram")
plt.show()