# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 23:04:50 2023

@author: Rania Helmy
"""

import math
import os
import random
import re
import sys

#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def marsExploration(s):
    # Write your code here
    result = 0
    mes = 'SOS'
    for i, c in enumerate(s):
        if c != mes[i%3]:
            result += 1
    return result
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
