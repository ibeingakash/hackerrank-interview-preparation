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
    p = s.split(":")
    p[0] = int(p[0])%12
    if "PM" in p[-1] and [0]:
        p[0]+=12
    p[0] = '%02d'%p[0]
    return ":".join(p)[:-2]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
