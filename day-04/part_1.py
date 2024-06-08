import re
import os

path = os.path.join(os.getcwd(), "day-04", "input.txt")
file = open(path)
cards = file.read().splitlines()

points = 0

for card in cards:
    winning_numbers = re.findall(r'\d+', card.split("|")[0].split(":")[1]) 
    playing_numbers = re.findall(r'\d+', card.split("|")[1])
    winning_count = 0
    
    for w_num in winning_numbers:
        if w_num in playing_numbers:
            winning_count += 1
    if winning_count:
        points += 2**(winning_count - 1)

print(points)