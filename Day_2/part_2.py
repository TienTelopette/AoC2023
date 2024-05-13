import numpy as np

file = open("C:/Users/ttche/Desktop/AoC2023/Day_2/input.txt","r")
games = file.read().splitlines()
powers = 0

def get_power_from_round(game):
    # Returns the power of the mins of each cube color from a row
    game_id = int(game.split(":")[0].split(" ")[1])
    game = game.split(":")[1]
    rounds = game.split(";")

    mins = dict()
    mins["red"] = -1
    mins["green"] = -1
    mins["blue"] = -1

    for round in rounds:
        cubes = round.split(",")
        for cube in cubes:
            split = cube.strip().split(" ")
            num = int(split[0].strip())
            color = split[1].strip()
            if mins[color] < num:
                mins[color] = num

    return np.prod(list(mins.values()))

for game in games:
    powers += get_power_from_round(game)
print(powers)