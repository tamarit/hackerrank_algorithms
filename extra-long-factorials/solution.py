#!/bin/python3
# https://www.hackerrank.com/challenges/extra-long-factorials/problem

import math
import os
import random
import re
import sys

#
# Complete the 'extraLongFactorials' function below.
#
# The function accepts INTEGER n as parameter.
#

def extraLongFactorials(n):
    # Write your code here
    if n == 0:
        return 1
    return n * extraLongFactorials(n - 1)

if __name__ == '__main__':
    n = int(input().strip())
    print(extraLongFactorials(n))
