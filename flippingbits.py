# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 23:29:27 2023

@author: Rania Helmy
"""

import math
import os
import random
import re
import sys

#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def flippingBits(n):
    # Write your code here
    x = '{:032b}'.format(n)
    fbits = "".join(['0' if i == '1' else '1' for i in x])
    n = int(fbits,2)
    return n

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()

