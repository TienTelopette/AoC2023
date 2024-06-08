import os
path = os.path.join(os.getcwd(), "day-02", "input.txt")
file = open(path)

games = file.read().splitlines()

cubes = dict()
cubes["red"] = 12
cubes["green"] = 13
cubes["blue"] = 14

valid_games_counter = 0

def check_cube(number_of_cubes, color):
    return cubes[color] >= number_of_cubes

def get_valid_game_id(game):
    game_id = int(game.split(":")[0].split(" ")[1])
    game = game.split(":")[1]
    rounds = game.split(";")

    for round in rounds:
        round = round.strip()
        for cube in round.split(","):
            cube = cube.strip().split(" ")
            if not check_cube(int(cube[0]), cube[1]):
                return 0
    
    return game_id

for game in games:
    valid_games_counter += get_valid_game_id(game)

print(valid_games_counter)