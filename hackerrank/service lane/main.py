#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'serviceLane' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY cases
#

def serviceLane(n, cases, width):
    # Write your code here
    ans = []
    for case in cases:
        ans.append(min(width[int(case[0]) : int(case[1])+1]))
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    width = list(map(int, input().rstrip().split()))

    cases = []

    for _ in range(t):
        cases.append(list(map(int, input().rstrip().split())))

    result = serviceLane(n, cases, width)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
