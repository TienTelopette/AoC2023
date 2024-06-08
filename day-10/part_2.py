import numpy as np
import os

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

def get_neighbours(pos, map):
    directions = []
    left = (pos[0], pos[1] - 1) if map[pos[0]][pos[1] - 1] not in (-1, 1) else None
    right = (pos[0], pos[1] + 1) if map[pos[0]][pos[1] + 1] not in (-1, 1) else None
    up = (pos[0] - 1, pos[1]) if map[pos[0] - 1][pos[1]] not in (-1, 1) else None
    down = (pos[0] + 1, pos[1]) if map[pos[0] + 1][pos[1]] not in (-1, 1) else None
    
    next_pos = [left, right, up, down]
    return [pos for pos in next_pos if pos]


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

VERTICES = ["F", "7", "L", "J"]


matrix = np.pad(matrix, (1,1), "constant", constant_values=".") # padding matrix with .
start_pos = tuple(np.argwhere(matrix == "S")[0])
current_pos = start_pos
first_moves, first_directions = get_first_moves(matrix, current_pos)
current_pos = first_moves[0]
current_char = matrix[current_pos[0], current_pos[1]]
direction = first_directions[0]
vertices = [start_pos]
boundary_points = 1

while current_char != "S":
    # moves to next position using direction and current_pos and updating the corresponding steps_matrix
    direction = get_next_direction(direction, current_pos)
    current_pos = get_next_pos(direction, current_pos)
    if matrix[current_pos[0]][current_pos[1]] in VERTICES:
        vertices.append(current_pos)
    boundary_points += 1
    current_char = matrix[current_pos[0]][current_pos[1]]

vertices.append(start_pos)

def get_area(vertices):
    area = 0
    for i in range(0,len(vertices) - 1):
        a = np.column_stack((vertices[i], vertices[i + 1]))
        det = np.linalg.det(a)
        area += int(round(det))
    
    return np.abs(area / 2)


area = get_area(vertices)
solution = area - (boundary_points / 2) + 1
print(solution)