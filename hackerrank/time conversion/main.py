#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    hour = s[:2]
    minutes = s[3:5]
    seconds = s[6:8]
    d = s[8:]
    if d == "AM":
        if hour == "12":
            hour = "00"
        return f"{hour}:{minutes}:{seconds}"
    else:
        if hour == "12":
            hour = "0"
        return f"{int(hour)+12}:{minutes}:{seconds}"

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    print(result)

    # fptr.write(result + '\n')

    # fptr.close()
