# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 08:31:52 2019

@author: dbda
"""

import pandas as pd

mydata = pd.read_csv("uforeports.dat")
type(mydata)
#print(mydata.City)
#print(mydata["City"])

mydata["Location"] = mydata.City + ", " + mydata.State
print(mydata.columns)

mydata2 = pd.read_csv("D:\dbda\py\imdb_1000.csv")
print(mydata2.describe())
print(mydata2.info())
print(mydata2.shape)
print(mydata2.genre.unique())
