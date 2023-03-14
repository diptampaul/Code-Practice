#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'chocolateFeast' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER c
#  3. INTEGER m
#

def chocolateFeast(n, c, m):
    # Write your code here
    total_chocolates = 0
    chocolate_in_hand = n//c
    total_chocolates += chocolate_in_hand
    while chocolate_in_hand != 0:
        chocolate_can_buy = chocolate_in_hand // m
        if chocolate_can_buy == 0:
            break
        chocolate_in_hand = chocolate_can_buy + (chocolate_in_hand % m)
        total_chocolates += chocolate_can_buy
    return total_chocolates

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        c = int(first_multiple_input[1])

        m = int(first_multiple_input[2])

        result = chocolateFeast(n, c, m)

        print(result)

    #     fptr.write(str(result) + '\n')

    # fptr.close()
