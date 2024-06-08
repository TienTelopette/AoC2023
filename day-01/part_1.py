import re
import os
path = os.path.join(os.getcwd(), "day-01", "input.txt")
file = open(path)
lines = file.readlines()

def get_line_digit(line):
   # returns first number found from line
   return re.search(r"\d+", line).group()

def get_line_values(lines):
    # returns list of first and last number of each line
    lines_values = [int(get_line_digit(line) + get_line_digit(line[::-1])) for line in lines]
    return lines_values

lines_values_total = get_line_values(lines)

print(sum(lines_values_total))