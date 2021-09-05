#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    arr.sort()
    a = sum(arr)
    max = a - arr[0]
    min = a - arr[len(arr)-1]
    print(min, max)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))
    

    miniMaxSum(arr)
