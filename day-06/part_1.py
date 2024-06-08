import re
import os

path = os.path.join(os.getcwd(), "day-06", "input.txt")
file = open(path)
Games = file.read().splitlines()
INPUT_TIMES = [int(time) for time in re.findall(r"\d+",Games[0])]
INPUT_RECORDS = [int(distance) for distance in re.findall(r"\d+",Games[1])]
NUMBER_OF_GAMES = len(INPUT_TIMES)
solution = 1

# Distance = Button_press * (Time - Button_press)
for game in range(NUMBER_OF_GAMES):
    RECORD_DISTANCE = INPUT_RECORDS[game]
    TIME = INPUT_TIMES[game]
    Distances = []

    Distances = [button_press * (TIME - button_press) for button_press in range(1, TIME + 1)]
    win_counts = 0

    for dist in Distances:
        if dist > RECORD_DISTANCE:
            win_counts += 1
    solution *= win_counts

print(solution)

