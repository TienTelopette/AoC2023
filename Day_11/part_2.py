import numpy as np

def get_empty_rows_cols(m): # returns list of empty rows and cols numbers
    empty_rows = []
    empty_cols = []
    for i in range(m.shape[0]): # iterate over rows
        where = m[i,:] == "#"
        if not where.any():
            empty_rows.append(i)
    for j in range(m.shape[0]): # iterate over cols
        where = m[:,j] == "#"
        if not where.any():
            empty_cols.append(j)
    
    return empty_rows, empty_cols

file = open("/Users/Tien/Documents/GitHub/AoC2023/Day_11/input.txt","r")
data = [[*string] for string in file.read().splitlines()]

m = np.matrix(data)


empty_rows, empty_cols = get_empty_rows_cols(m)

coords = np.where(m == "#")
galaxies = []

for x, y in zip(coords[0], coords[1]):
    galaxies.append((x,y))

solution = 0
for start in galaxies:
    for end in galaxies[(galaxies.index(start) + 1):]:
        row_expansions = 0
        col_expansions = 0
        row_range = range(min(start[0], end[0]), max(start[0], end[0]))
        col_range = range(min(start[1], end[1]), max(start[1], end[1]))
        for row in empty_rows:
            if row in row_range:
                row_expansions += 1

        for col in empty_cols:
            if col in col_range:
                col_expansions += 1
        
        solution += abs(start[0] - end[0]) + abs(start[1] - end[1]) + (row_expansions + col_expansions) * 999999

print(solution)