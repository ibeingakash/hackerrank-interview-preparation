#!/bin/python3

import math
import os
import random
import re
import sys



def plusMinus(arr):
    pos = 0
    neg = 0
    zer = 0
    for i in arr:
        if i>0:
            pos +=1
        elif i==0:
            zer +=1
        else:
            neg +=1
        
    print(pos/n)
    print(neg/n)
    print(zer/n)
    
            

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
