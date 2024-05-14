import re
file = open("/Users/Tien/Documents/GitHub/AoC2023/Day_6/input.txt","r")
Games = file.read().splitlines()
INPUT_TIME = int("".join([time for time in re.findall(r"\d+",Games[0])]))
INPUT_RECORD = int("".join([distance for distance in re.findall(r"\d+",Games[1])]))

# Distance = button_press * (Time - button_press)
Distances = [button_press * (INPUT_TIME - button_press) for button_press in range(1, INPUT_TIME + 1)]
wins = len([dist for dist in Distances if dist > INPUT_RECORD])

print(wins)
