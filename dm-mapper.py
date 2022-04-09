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
    # À compléter
    if matrixname =="A":
     for i in range(n):
      print ("(%s,%s)\t%s\t%s"%(x,i,y,matrixvalue))
    else:
      for i in range(n):
       print ("(%s,%s)\t%s\t%s"%(i,y,x,matrixvalue))    
file1.close()
file2.close()       