#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Reducer to compute Matrix product A*B = C, where A,B are nxn matrices.
More specifically, reducer computes one value of C, i.e. a sum of the form
sum_k a_i,j*b_k,j
Assumes mapper sent pairs (key,value):
where 
- key = 
- value = 
"""

import sys
from collections import defaultdict
from unittest import result

file1 = open('resultmap.txt', 'r')
file2 = open("resultreduce.txt", "w")
Lines = file1.readlines()
sys.stdout=file2
prev_k = None
d = defaultdict(list)  # you may use a dict, or d=[1]*n. Dict is some kind of an optimization for sparse matrices. But the bottleneck of our algorithm is the shuffle anyway.

for line in Lines:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    key,key2,value = line.split('\t', 2)
    # À compléter ...
    d[key].append((key2,int(value))) 
    d[key].sort(key = lambda x: x[0]) 
for cle, valeur in d.items():
    cumul=0
    for i in range((len(valeur)//2)):
        cumul+=valeur[2*i][1]*valeur[2*i+1][1]
    print ("%s\t%s"%(cle,cumul))      
file1.close()
file2.close()    