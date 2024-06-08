import os

path = os.path.join(os.getcwd(), "day-09", "input.txt")
file = open(path)
Numbers = file.read().splitlines()
Numbers = [[int(n) for n in line.split(" ")] for line in Numbers]
solution = 0

def get_extrapolation(Numbers):
    Result = []
    for n in range(len(Numbers) - 1):
        Result.append(Numbers[n + 1] - Numbers[n])
    return Result

def algorithm(Extrapolations):
    Extrapolations = Extrapolations[::-1]
    for n in range(len(Extrapolations) - 1):
        Extrapolations[n + 1].reverse()
        Extrapolations[n + 1].append(Extrapolations[n + 1][-1] - Extrapolations[n][-1])
    print(Extrapolations)


for i in range(len(Numbers)):
    Extrapolations = [Numbers[i]]
    extrapolation = get_extrapolation(Numbers[i])
    while any(extrapolation):
        Extrapolations.append(extrapolation)
        extrapolation = get_extrapolation(extrapolation)
    algorithm(Extrapolations)
    solution += Extrapolations[0][-1]


print(solution)