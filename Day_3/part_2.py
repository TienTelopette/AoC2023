import numpy as np
import re
from scipy.ndimage import grey_dilation, iterate_structure

file = open("C:/Users/ttche/Desktop/AoC2023/Day_3/input.txt","r")
rows = file.read().splitlines()
size = len(rows[0])
res = 0

def get_sum_of_full_numbers(rows, star_coords):
    dict_star_numbers = dict()
    # tuples of (row, start_index, end_index, value)
    all_numbers_coords = []
    sum = 0

    # Populate all_numbers_coords with tuples containing position and value of all the full numbers
    for i in range(len(rows)):
        for match in re.finditer(r"\d+", rows[i]):
            start_index = match.start(0)
            end_index = match.end(0) - 1
            all_numbers_coords.append((i, start_index, end_index, int(match.group(0))))        

    # Add to dict_star_numbers with key = star_coord and values = [all number tuples adjacent to the star]
    for star_coord in star_coords:
        for number_coord in all_numbers_coords:
            row_range = range(star_coord[0] - 1, star_coord[0] + 2)
            col_range = range(star_coord[1] - 1, star_coord[1] + 2)
            # Add to dictionary with key = star_coord if the number is neighbour of the star
            if number_coord[0] in row_range and ((number_coord[1] in col_range) or (number_coord[2] in col_range)):
                if star_coord not in dict_star_numbers:
                    dict_star_numbers[star_coord] = [number_coord[3]]
                else:
                    dict_star_numbers[star_coord].append(number_coord[3])
    return dict_star_numbers


matrix = np.empty(shape=(size,size), dtype=str)
for i in range(0, size):
    matrix[i] = [*rows[i]]


# Find all star coordinates and put them in star_coords
star_coords = []
for row in range(size):
    for col in range(size):
        char = matrix[row][col]
        if char == "*":
            star_coords.append((row, col))

dict_star_numbers = (get_sum_of_full_numbers(rows, star_coords))

# add to res the product of all pairs of numbers adjacent to a star
for values in dict_star_numbers.values():
    if len(values) == 2:
        res += np.prod(values)
print(res)