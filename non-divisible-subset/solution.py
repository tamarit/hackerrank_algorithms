#!/bin/python3
# https://www.hackerrank.com/challenges/non-divisible-subset

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
    # Write your code here
    remainderArr = [0] * k
    for i in s:
        remainderArr[i % k] += 1

    
    maxLength = 0
    # In the worst case, e.g. if k = 1, we can build a subset with a single element
    # which fullfills the requirements
    maxLength += min(remainderArr[0], 1)

    for i in range(1, k//2+1):
        if i == k-i:
            # This only happens when k is even
            # I cannot take two elements with this remainder because they 
            # would add up to k, i.e. they would be divisible by k
            maxLength += min(
                remainderArr[i],
                1
            )
        else:
            # Nothe that i + (k - i) = k, so we can only add one of them.
            # Therefore we add the largest one
            maxLength += max(
                remainderArr[i],
                remainderArr[k - i]
            )

    return maxLength



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()