file = open("/Users/Tien/Documents/GitHub/AoC2023/Day_8/input.txt","r")
data = file.read()
split = data.split("\n\n")
MOVESET = split[0].replace("L", "0").replace("R", "1")
Rules = split[1].splitlines()
now = "AAA"
DESTINATION = "ZZZ"
steps = 0
RULES = {s.split(" = ")[0]: s.split(" = ")[1].replace("(", "").replace(")", "").split(", ") for s in Rules}

while now != DESTINATION:
    for move in MOVESET:
        now = RULES[now][int(move)]
        steps += 1
        if now == DESTINATION:
            break

print(steps)