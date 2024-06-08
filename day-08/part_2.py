import numpy as np
import os

path = os.path.join(os.getcwd(), "day-08", "input.txt")
file = open(path)
data = file.read()
split = data.split("\n\n")
MOVESET = split[0].replace("L", "0").replace("R", "1")
Rules = split[1].splitlines()
Start_nodes = []
steps = 0
RULES = {s.split(" = ")[0]: s.split(" = ")[1].replace("(", "").replace(")", "").split(", ") for s in Rules}
Steps_to_z = []
Steps_to_second_z = []
Steps_to_third_z = []
got_to_z = False

# true is node ends with Z
def z_in_destination(node):
    return node[-1] == "Z"

# get all nodes ending with A and append in Start_nodes
for key in RULES.keys():
    if key[-1] == "A":
        Start_nodes.append(key)

for node in Start_nodes:
    got_to_z = False
    steps = 0
    while not got_to_z:
        for move in MOVESET:
            node = RULES[node][int(move)]
            steps += 1
            if z_in_destination(node):
                Steps_to_z.append(steps)
                got_to_z = True
    

print(Steps_to_z)
print(np.lcm.reduce(Steps_to_z))