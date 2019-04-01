import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
mydata1=pd.read_csv("https://bit.ly/uforeports")
print(mydata1.head(20))
print(mydata1.tail(20))
print(type(mydata1))
print(len(mydata1.index))
print(mydata1.shape)
m=mydata1.iloc[0:,3:]
print(m)
f=mydata1.loc[:5,['City','Shape Reported']]
print(f)
