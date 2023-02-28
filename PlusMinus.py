# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 11:47:00 2023

@author: Rania Helmy
"""

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    print("%.6f" %(len([x for x in arr if x>0])/n))
    print("%.6f" %(len([x for x in arr if x<0])/n))
    print("%.6f" %(len([x for x in arr if x==0])/n))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
