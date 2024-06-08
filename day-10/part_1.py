import os
import numpy as np

def get_next_pos(direction, pos):
    # direction = where to move next, pos = current position, returns tuple of next position
    res = [pos[0], pos[1]] # res = coordinates (row, col)

    if direction in ("up", "down"):
        res[0] += 1 if direction == "down" else -1
    else:
        res[1] += 1 if direction == "right" else -1

    return tuple(res)

def get_first_moves(matrix, pos):
    # returns list of 2 next possible positions from S and respective direction with respect to pos
    directions = []
    left = (pos[0], pos[1] - 1) if ("left", matrix[pos[0]][pos[1] - 1]) in MOVES.keys() else None
    if left:
        directions.append("left")
    right = (pos[0], pos[1] + 1) if ("right", matrix[pos[0]][pos[1] + 1]) in MOVES.keys() else None
    if right:
        directions.append("right")
    up = (pos[0] - 1, pos[1]) if ("up", matrix[pos[0] - 1][pos[1]]) in MOVES.keys() else None
    if up:
        directions.append("up")
    down = (pos[0] + 1, pos[1]) if ("down", matrix[pos[0] + 1][pos[1]]) in MOVES.keys() else None
    if down:
        directions.append("down")
    
    next_pos = [left, right, up, down]

    return [pos for pos in next_pos if pos], directions

def get_next_direction(direction, pos):
    return MOVES[(direction, matrix[pos[0]][pos[1]])]

path = os.path.join(os.getcwd(), "day-10", "input.txt")
file = open(path)
data = file.read().splitlines()
data = [list(row)for row in data]
matrix = np.matrix(data)
MOVES = {("up", "|"): "up",
         ("up", "F"): "right", 
         ("up", "7"): "left",
         ("down", "|"): "down", 
         ("down", "L"): "right",
         ("down", "J"): "left",
         ("left", "-"): "left",
         ("left", "L"): "up",
         ("left", "F"): "down",
         ("right","-") : "right",
         ("right", "J"): "up",
         ("right", "7"): "down"}

ALLOWED = {"right": ["-", "J", "7"], 
           "left": ["-", "L", "F"],
           "down": ["|", "L", "J"], 
           "up": ["|", "F", "7"]}


matrix = np.pad(matrix, (1,1), "constant", constant_values=".") # padding matrix with .
steps_matrix = [np.zeros(matrix.shape, dtype = int), np.zeros(matrix.shape, dtype = int)] # steps to each cell from S for each direction
start_pos = tuple(np.argwhere(matrix == "S")[0])
current_pos = start_pos
first_moves, first_directions = get_first_moves(matrix, current_pos)

for i in range(len(first_moves)):
    # do once for each direction
    steps = 1    
    current_pos = first_moves[i]
    direction = first_directions[i]
    current_char = matrix[current_pos[0], current_pos[1]]
    steps_matrix[i][current_pos[0]][current_pos[1]] = 1

    while current_char != "S":
        # moves to next position using direction and current_pos and updating the corresponding steps_matrix
        direction = get_next_direction(direction, current_pos)
        current_pos = get_next_pos(direction, current_pos)
        current_char = matrix[current_pos[0]][current_pos[1]]
        steps += 1
        steps_matrix[i][current_pos[0]][current_pos[1]] += steps



steps_matrix[0][steps_matrix[0] == 0] = -1
res = steps_matrix[0] - steps_matrix[1]

where = np.where(res == 0)
final_pos = [(where[0][0], where[1][0]), (where[0][1], where[1][1])] # only two cells with 0, one is S

for f in final_pos:
    if f != start_pos:
        print(steps_matrix[0][f[0]][f[1]])
    