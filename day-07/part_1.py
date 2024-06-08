import re
import pandas as pd
import os

path = os.path.join(os.getcwd(), "day-07", "input.txt")
file = open(path)
Hands = file.read().splitlines()
Cards = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
CARDS = {card: value for value, card in enumerate(Cards, 2)}


def get_occurrences_and_remove(to_remove, string):
    occurrences = string.count(to_remove)
    result = string.replace(to_remove, "")
    return result, occurrences

data = dict()
labels = ["hand", "bid", "occurrences"]
data["hand"] = []
data["bid"] = []
data["occurrences"] = []
data["values"] = []


for hand in Hands:
    temp_hand = hand.split(" ")[0]
    temp_occurrences = []
    bid = int(hand.split(" ")[1])
    data["hand"].append(temp_hand)
    data["values"].append([CARDS[card] for card in temp_hand])

    while temp_hand:
        temp_hand, occurrences = get_occurrences_and_remove(temp_hand[0], temp_hand)
        temp_occurrences.append(occurrences)
    
    data["bid"].append(int(bid))
    data["occurrences"].append("".join(str(a) for a in sorted(temp_occurrences, reverse = True)))

cards = pd.DataFrame(data)
cards = cards.sort_values(by = "occurrences", ascending = False).reset_index(drop = True)

result = pd.DataFrame(columns = labels)
for name, group in cards.groupby(by = "occurrences", sort=False):
    temp = group.sort_values(by = "values", ascending = False)
    result = pd.concat([result, temp])


result = result.iloc[::-1]

bids = result.bid.tolist()
points = 0
[points := points + bids[i] * (i + 1) for i in range(len(bids))]
print(points)
