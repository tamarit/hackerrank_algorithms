#!/bin/python3
# https://www.hackerrank.com/challenges/the-time-in-words

import math
import os
import random
import re
import sys

#
# Complete the 'timeInWords' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER h
#  2. INTEGER m
#

def convert_number_to_str(n):
    def digit(d):
        match d:
            case 0:
                return ""
            case 1:
                return "one"
            case 2:
                return "two"
            case 3:
                return "three"
            case 4:
                return "four"
            case 5:
                return "five"
            case 6:
                return "six"
            case 7:
                return "seven"
            case 8:
                return "eight"
            case 9:
                return "nine"
    if n < 10:
        return digit(n)
    elif n < 20:
        match n:
            case 11:
                return "eleven"
            case 12:
                return "twelve"
            case 13:
                return "thirteen"
            case 14:
                return "fourteen"
            case 15:
                return "quarter"
        return digit(n % 10) + "teen"
    elif n == 30:
        return "half"
    elif n < 30:
        return "twenty " + digit(n % 20)
    elif n < 40:
        return "thirty " + digit(n % 30)
    elif n < 50:
        return "forty " + digit(n % 40)
    elif n < 60:
        return "fifty " + digit(n % 50)
            

def timeInWords(h, m):
    # Write your code here
    if m == 0:
        return convert_number_to_str(h) + " o' clock"
    if m <= 30:
        minutes_term = "" if m in [15,30] else " minutes" if m > 1 else " minute"
        return  f"{convert_number_to_str(m)}{minutes_term} past {convert_number_to_str(h)}" 
    rm = 60 - m
    minutes_term = "" if rm in [15,30] else " minutes" if rm > 1 else " minute"
    next_hour = h + 1 if h < 12 else 1
    return  f"{convert_number_to_str(rm)}{minutes_term} to {convert_number_to_str(next_hour)}" 


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input().strip())

    m = int(input().strip())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
