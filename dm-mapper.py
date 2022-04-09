#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

n=2
file1 = open('entree-matrices.txt', 'r')
file2 = open("resultmap.txt", "w")
Lines = file1.readlines()
sys.stdout=file2

for line in Lines:

### for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    k,v = line.split('\t',1)
    x,y,matrixname,matrixvalue = eval(v)
    # create a key value data for reduce
    # key will be (a,b): a is the line the the value should be used , b is the column the the value should be used 
    if matrixname =="A":
     # value is used n times so it needs to be duplicated n times 
     for i in range(n):
      print ("(%s,%s)\t%s\t%s"%(x,i,y,matrixvalue))
    else:
      for i in range(n):
       print ("(%s,%s)\t%s\t%s"%(i,y,x,matrixvalue))    
file1.close()
file2.close()       