import re
file = open("C:/Users/ttche/Desktop/AoC2023/Day_4/input.txt","r")
cards = file.read().splitlines()
limit = len(cards)

total_cards = [1 for i in range(limit)]
points = 0
i = 0

for card in cards:
    winning_numbers = re.findall(r'\d+', card.split("|")[0].split(":")[1]) 
    playing_numbers = re.findall(r'\d+', card.split("|")[1])
    winning_count = 0
    
    for w_num in winning_numbers:
        if w_num in playing_numbers:
            winning_count += 1
    j = i
    while winning_count and j < limit:
        total_cards[j + 1] += total_cards[i]
        j += 1
        winning_count -= 1

    i += 1
print(sum(total_cards))