#!/bin/python3
# https://www.hackerrank.com/challenges/organizing-containers-of-balls

import math
import os
import random
import re
import sys

#
# Complete the 'organizingContainers' function below.
#
# The function is expected to return a STRING.
# The function accepts 2D_INTEGER_ARRAY container as parameter.
#

def organizingContainers(container):
    # Write your code here
    sorted_sum = lambda l: sorted([sum(x) for x in l])
    return (
        "Possible" 
        if sorted_sum(container) == sorted_sum(zip(*container)) else 
        "Impossible"
    )


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        fptr.write(result + '\n')

    fptr.close()
