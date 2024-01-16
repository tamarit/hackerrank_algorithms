#!/bin/python3
# https://www.hackerrank.com/challenges/two-pluses

import math
import os
import random
import re
import sys

#
# Complete the 'twoPluses' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY grid as parameter.
#

def twoPluses(grid):
    max_plus_list = []
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            # print((row, col))
            # print(grid[row][col])
            if grid[row][col] == 0:
                # print(0)
                continue
            i = 1
            # max_plus = 1
            max_plus_list.append((1, (row, col)))
            while (
                row - i >= 0 and 
                col - i >= 0 and 
                row + i < len(grid) and 
                col + i < len(grid[row])
            ):
                if sum([
                    grid[row - i][col], 
                    grid[row + i][col], 
                    grid[row][col - i], 
                    grid[row][col + i]
                ]) != 4:
                    break
                # max_plus += 4
                max_plus_list.append((1 + (i * 4), (row, col)))
                i += 1
            # max_plus_list.append((max_plus, (row, col)))
    max_plus_list = sorted(max_plus_list, key=lambda x: x[0], reverse=True)
    # print(max_plus_list)
    def get_busy_cells(plus_data):
        busy_cells = [plus_data[1]]
        for i_ in range(plus_data[0]//4):
            i = 1 + i_
            busy_cells.append((plus_data[1][0] - i, plus_data[1][1]))
            busy_cells.append((plus_data[1][0] + i, plus_data[1][1]))
            busy_cells.append((plus_data[1][0], plus_data[1][1] - i))
            busy_cells.append((plus_data[1][0], plus_data[1][1] + i))
        return set(busy_cells)

    max_products = []
    for start in range(len(max_plus_list) - 1):
        # print(f"START {start}")
        selected_plus = max_plus_list[start]
        busy_cells_selected = get_busy_cells(selected_plus)
        # print(busy_cells_selected)
        for second_plus in max_plus_list[start + 1:]:
            # print(second_plus)
            # print(get_busy_cells(second_plus))
            # print(busy_cells_selected.intersection(get_busy_cells(second_plus)) )
            if busy_cells_selected.intersection(get_busy_cells(second_plus)) == set():
                # print(f"APPENDED {selected_plus[0] * second_plus[0]}")
                max_products.append(selected_plus[0] * second_plus[0])
                break 
    return max(max_products)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    grid = []

    for _ in range(n):
        grid_item = input()
        # grid.append(grid_item)
        grid.append(list(map(lambda gi:1 if gi == 'G' else 0, grid_item)))

    result = twoPluses(grid)

    fptr.write(str(result) + '\n')

    fptr.close()
