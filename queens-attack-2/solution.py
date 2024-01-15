#!/bin/python3
# https://www.hackerrank.com/challenges/queens-attack-2/problem

import math
import os
import random
import re
import sys

#
# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles
#

def queensAttack(n, k, r_q, c_q, obstacles):
    # Write your code here
    r_q = r_q - 1
    c_q = c_q - 1
    obstacles = set([(r - 1, c - 1) for r, c in obstacles])
    counter = 0

    # ver_up
    for i in range(1, (n - r_q)):
        if (r_q + i, c_q) in obstacles:
            break
        counter += 1

    # ver_down
    for i in range(1, r_q + 1):
        if (r_q - i, c_q) in obstacles:
            break
        counter += 1

    # hor_right
    for i in range(1, (n - c_q)):
        if (r_q, c_q + i) in obstacles:
            break
        counter += 1
        
    # hor_left
    for i in range(1, c_q + 1):
        if (r_q, c_q - i) in obstacles:
            break
        counter += 1

    # diag_up_right
    for i in range(1, min(n - r_q, n - c_q)):
        if (r_q + i, c_q + i)  in obstacles:
            break
        counter += 1

    # diag_down_left
    for i in range(1, min(r_q, c_q) + 1):
        if (r_q - i, c_q - i) in obstacles:
            break
        counter += 1

    # diag_up_left
    for i in range(1, min(n - r_q, c_q + 1)):
        if (r_q + i, c_q - i) in obstacles:
            break
        counter += 1

    # diag_down_right
    for i in range(1, min(r_q + 1, n - c_q)):
        if (r_q - i, c_q + i) in obstacles:
            break
        counter += 1

    return counter



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    r_q = int(second_multiple_input[0])

    c_q = int(second_multiple_input[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
