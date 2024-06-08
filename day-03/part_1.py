import numpy as np
import re
from scipy.ndimage import grey_dilation, iterate_structure
import os
path = os.path.join(os.getcwd(), "day-03", "input.txt")
file = open(path)
rows = file.read().splitlines()
size = len(rows[0])

def set_symbol_neighbours_true(input):
    # Binary dilates all the already present True positions by 1
    st = np.full((3, 3), True)
    ret = grey_dilation(input, footprint = iterate_structure(st,1))
    return ret

def get_sum_of_full_numbers(rows, map):
    # Gives the sum of all the numbers neighbours of a symbol
    sum = 0
    for row in range(size):
        for match in re.finditer(r"\d+", rows[row]):
            start_index = match.start(0)
            end_index = match.end(0)
            number_to_sum = 0
            for i in range(start_index, end_index):
                if(map[row][i]):
                    number_to_sum = int(match.group(0))
            sum += number_to_sum
        
    return sum


matrix = np.empty(shape=(size,size), dtype=str)
for i in range(0, size):
    matrix[i] = [*rows[i]]

map = np.full((size, size), False)

# On boolean matrix map set all the positions relative to symbols to True
for row in range(size):
    for col in range(size):
        char = matrix[row][col]
        if char != "." and not char.isdigit():
            map[row][col] = True

# Binary dilation of the True positions
map = set_symbol_neighbours_true(map)

print(get_sum_of_full_numbers(rows, map))
