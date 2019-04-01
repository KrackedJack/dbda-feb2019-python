# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 00:50:22 2019

@author: anilk
"""
print("Hello World!");

#import libraries
import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.svm import SVR

dates=[]
prices=[]

def get_data(filename):
    with open(filename,'r') as csvfile:
        csvFileReader=csv.reader(csvfile)
        next(csvFileReader)  #this will read first row helps in skipping first row. its header
        for row in csvFileReader:
            dates.append(int(row[0].split('-')[0]))
            prices.append(float(row[1]))
    return

def predict_price(dates,prices,x):
    dates=np.reshape(dates,(len(daes),1))  #use numpy to create nX1 formated list
    #Lets create three models
    #each of them is type of support vector machine
    #a support vector machine is a linear separator it takes data that is already classified
    #and try to prdict a set of unclassified data so if we only had two data classes 
    #it will be the line such that the distances from the closest points in each of the two groups would
    #be farthest away when we add new point to our graph depending on which side of the line it is we could classify accordingly with a label
    #but right now we are not predicting a class label so we don't need to classify instead we are predicting the  
    #next value in the series which means we want to use regression
    #SVM's can be used for regression as well
    #the support vector regression is a type of SVM that uses the space between data as a margin of error and prdicts the most likely next point in the data set
    #lets create first model a linear support vector regression well use the svr module we imported from sci-kit learn
    #We are passing 2 parameters
    #1. kernel - type of SVM
    #2. C - penalty parameter of the error term
    #we want 2 things when using svr aligned with the largest minimum margin in a line that correctly separates as many instances as possible
    #but we always can't have both
    #c determines how much we want to latter
    
    svr_li
    n=SVR(kernel="linear", C=1e3)
    svr_poly=SVR(kernel='poly',C=1e3)
    svr_rbf=SVR(kernel='rbf',C=1e3,gamma=0.1)
    #next model in SVR is polynomial in math folklore the no free lunch theorum states that
    #there are no gu#arentees for one optimization to work better
    #than other so we will try both
    #we will create one more SVR using radial basis function
    #rbf defined similarity to be the Euclidean distance between 2 i/p
    #if both are right on top of each other the max similarity is 1 if too far its 0
    #our gamma defines how far to far is and lets fit or train each of our models on date and price data
    #using fit method
    svr_lin.fit(dates,prices)
    svr_poly.fit(dates,prices)
    svr_rbf.fit(dates,prices)
    #now lets create graph
    plt.scatter(dates,prices,color='black',label='Data')
    #prdict method of the svr object in sklearn using dates matrix
    plt.plot(dates,svr_rbf.predict(dates),color='red',label='rbf model')
    plt.plot(dates,svr_lin.predict(dates),color='green',label='linear model')
    plt.plot(dates,svr_poly.predict(dates),color='blue',label='poly model')
    plt.xlabel('Date')
    plt.ylabel('price')
    plt.title("support vector regression")
    plt.legend()
    
    plt.show()
    return svr_rbf.predict(x)[0],svr_lin.predict(x)[0],svr_poly.predict(x)[0]

get_data('aapl.csv')
predicted_price=predict_prices(dates,prices,29)
print("price : ",predicted_price)
#graph shows our rbf model fits better
#so we can use its value
#this prediction is better than random if we use right data
#SVM can be used for both classification ad regression to predict



    
    
    
    
    
    
    
            
        
    




