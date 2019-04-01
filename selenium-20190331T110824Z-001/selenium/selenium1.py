# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 17:58:04 2019

@author: anilk
"""
print("Hello World!");

#import libraries
import sys
sys.path.append(r"C:\mydata\python bnp\extrademo\selenium\geckodriver-v0.24.0-win64")
from selenium import webdriver
import time
''' 
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.binary_location =r".\chromedriver_win32"
driver = webdriver.Chrome(chrome_options=options, executable_path=r'C:\mydata\webdriver_selenium\chromedriver_win32\')
'''
driver=webdriver.Firefox(executable_path = 'C:\mydata\python bnp\extrademo\selenium\geckodriver-v0.24.0-win64\geckodriver')
driver.get('https://python.org')


