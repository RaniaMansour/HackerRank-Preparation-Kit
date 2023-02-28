# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 22:08:23 2023

@author: Rania Helmy
"""
x = [5,3,8,4,1]
y = [8,4,3,5,2,7]

#import statistics
#print(statistics.median(x))
#print(statistics.median(y))

def median(arr):
    arr.sort()
    n = len(arr)
    if n % 2 == 0:
        median = (arr[n//2] + arr[n//2 -1])/2
    else:
        median = arr[n//2]
    return print(median)

median(y)
    
        