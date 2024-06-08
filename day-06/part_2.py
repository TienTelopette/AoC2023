import re
import os

path = os.path.join(os.getcwd(), "day-06", "input.txt")
file = open(path)
Games = file.read().splitlines()
INPUT_TIME = int("".join([time for time in re.findall(r"\d+",Games[0])]))
INPUT_RECORD = int("".join([distance for distance in re.findall(r"\d+",Games[1])]))

# Distance = button_press * (Time - button_press)
Distances = [button_press * (INPUT_TIME - button_press) for button_press in range(1, INPUT_TIME + 1)]
wins = len([dist for dist in Distances if dist > INPUT_RECORD])

print(wins)
