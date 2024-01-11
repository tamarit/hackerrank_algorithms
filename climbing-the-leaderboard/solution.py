#!/bin/python3
# https://www.hackerrank.com/skills-verification

import math
import os
import random
import re
import sys

# #
# # Complete the 'climbingLeaderboard' function below.
# #
# # The function is expected to return an INTEGER_ARRAY.
# # The function accepts following parameters:
# #  1. INTEGER_ARRAY ranked
# #  2. INTEGER_ARRAY player
# #
def climbingLeaderboard(ranked, player):
    ranked = sorted(set(ranked), reverse=True) 
    index = len(ranked)
    for player_score in player:
        while player_score >= ranked[index - 1] and index > 0:
            index -= 1
        yield index + 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
