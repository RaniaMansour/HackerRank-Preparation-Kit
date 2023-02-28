# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 21:57:24 2023

@author: Rania Helmy
"""
import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    # Write your code here
    import string
    if (''.join(sorted(set(s.lower().replace(" ","")))))==string.ascii_lowercase:
        return 'pangram'
    else:
        return 'not pangram'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
