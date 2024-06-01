import re
import pandas as pd

file = open("/Users/Tien/Documents/GitHub/AoC2023/Day_7/input.txt","r")
Hands = file.read().splitlines()
Cards = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]
CARDS = {card: value for value, card in enumerate(Cards, 2)}


def get_occurrences_and_remove(to_remove, string):
    # from string remove to_remove and return occurrences count
    # and return result string and occurrences count
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
    # process hands data to create a dataframe with occurrences = count of same cards
    # occurrences in hand, list of values of each card
    temp_hand = hand.split(" ")[0]
    temp_occurrences = []
    bid = int(hand.split(" ")[1])
    data["hand"].append(temp_hand)
    data["values"].append([CARDS[card] for card in temp_hand])
    jolly = temp_hand.count("J")

    while temp_hand:
        # iterate over each card and remove all occurrences of the same card
        # from hand and append number of occurrences to list
        to_check = temp_hand[0]
        temp_hand, occurrences = get_occurrences_and_remove(to_check, temp_hand)
        if to_check == "J": # Js are already counted by jolly
            continue
        temp_occurrences.append(occurrences)
    
    if not temp_occurrences:
        # special case JJJJJ
        temp_occurrences = [5]
    else:
        temp_occurrences[temp_occurrences.index(max(temp_occurrences))] += jolly
    
    data["bid"].append(int(bid))
    data["occurrences"].append("".join(str(a) for a in sorted(temp_occurrences, reverse = True)))

cards = pd.DataFrame(data)
cards = cards.sort_values(by = "occurrences", ascending = False).reset_index(drop = True)

result = pd.DataFrame(columns = labels)
for name, group in cards.groupby(by = "occurrences", sort = False):
    temp = group.sort_values(by = "values", ascending = False)
    result = pd.concat([result, temp])


result = result.iloc[::-1]
# print(result.loc[result["hand"] == "4"])
print(result)
bids = result.bid.tolist()
points = 0
[points := points + bids[i] * (i + 1) for i in range(len(bids))]
print(points)
