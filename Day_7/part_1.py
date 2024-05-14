import re
import pandas as pd

file = open("/Users/Tien/Documents/GitHub/AoC2023/Day_7/test_input.txt","r")
Hands = file.read().splitlines()

def get_occurrences_and_remove(to_remove, string):
    occurrences = string.count(to_remove)
    result = string.replace(to_remove, "")
    return result, occurrences

data = dict()
labels = ["hand", "bid", "occurrences"]
data["hand"] = []
data["bid"] = []
data["occurrences"] = []

for hand in Hands:
    temp_hand = hand.split(" ")[0]
    temp_duplicated_cards = []
    bid = int(hand.split(" ")[1])
    data["hand"].append(temp_hand)

    while temp_hand:
        temp_hand, occurrences = get_occurrences_and_remove(temp_hand[0], temp_hand)
        temp_duplicated_cards.append(occurrences)
    
    data["bid"].append(int(bid))
    data["occurrences"].append("".join(str(a) for a in sorted(temp_duplicated_cards, reverse = True)))

cards = pd.DataFrame(data)[labels]
cards = cards.sort_values(by = "occurrences", ascending = False)

for i in range(len(cards)):
    lst = cards.iloc[i,:]
    print(lst)


# def by_max_num_duplicates(l):
#     return max(l)

# Duplicated_cards.sort(key = by_max_num_duplicates)


