import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re

def clean(val):
       if not re.search('[a-zA-Z]', val): return int(val)
       else: return 0
    
with open("dataforMovie.txt") as file:
    data=pd.read_csv(file,sep="|",header=None, index_col=0,names=["Age","Gender","Job","Sal"])

    data["Concat"]=data['Age'].map(str)+":"+data['Job']
    
    data.Sal = data.Sal.apply(clean)
    
    print(data['Sal'].mean(), data.Sal.describe())
    
    