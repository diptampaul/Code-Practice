#!/bin/python3

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
    separation = {"p": [], "n": [], "z" : []}
    for n in arr:
        if n > 0:
            separation["p"] += [n]
        elif n == 0:
            separation["z"] += [n]
        else:
            separation["n"] += [n]
    
    for k,v in separation.items():
        print("%.6f" % (len(v)/len(arr)))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
