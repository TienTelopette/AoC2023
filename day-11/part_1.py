import numpy as np
import os

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
        


path = os.path.join(os.getcwd(), "day-11", "input.txt")
file = open(path)
data = [[*string] for string in file.read().splitlines()]

m = np.matrix(data)


empty_rows, empty_cols = get_empty_rows_cols(m)

for empty_row in empty_rows[::-1]:
    m = np.insert(m, empty_row, [*"."* m.shape[1]], axis=0)

for empty_col in empty_cols[::-1]:
    m = np.insert(m, empty_col, [*"."* m.shape[0]], axis=1)

coords = np.where(m == "#")
galaxies = []

for x, y in zip(coords[0], coords[1]):
    galaxies.append((x,y))

solution = 0
for start in galaxies:
    for end in galaxies[(galaxies.index(start) + 1):]:
        solution += abs(start[0] - end[0]) + abs(start[1] - end[1])
        
print(solution)