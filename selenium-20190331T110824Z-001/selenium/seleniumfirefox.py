# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 23:47:16 2019

@author: anilk
"""
print("Hello World!");

#import libraries
from selenium import webdriver
import time
driver=webdriver.Firefox(executable_path = 'C:\mydata\python bnp\extrademo\selenium\geckodriver-v0.24.0-win64\geckodriver')
driver.get('https://python.org')


