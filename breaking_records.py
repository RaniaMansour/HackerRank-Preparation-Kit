# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 13:01:37 2023

@author: Rania Helmy
"""

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    result = [0,0]
    lowest= scores[0]
    highest= scores[0]
    
    for i in range(1, len(scores)):
        if scores[i] < lowest:
            result[1] += 1
            lowest = scores[i]
            continue
        elif scores[i] > highest:
            result[0] += 1
            highest = scores[i]
            continue
    return result


    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
