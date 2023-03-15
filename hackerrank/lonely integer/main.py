#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    # Write your code here
    u = {}
    for item in a:
        if item not in u:
            u[item] = 1
        else:
            u[item] = u[item] + 1
    
    for k,v in u.items():
        if v == 1:
            return k


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
