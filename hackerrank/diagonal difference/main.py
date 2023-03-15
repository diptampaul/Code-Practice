#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    first_sum = 0
    second_sum = 0

    last_column = len(arr[0]) - 1
    for i in range(len(arr[0])):
        for j in range(len(arr)):
            if i == j:
                first_sum += arr[i][j]
                second_sum += arr[i][last_column]
                last_column -= 1

    return abs(first_sum - second_sum)

            


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
