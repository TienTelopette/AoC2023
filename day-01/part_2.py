import re
import os
path = os.path.join(os.getcwd(), "day-01", "input.txt")
file = open(path)

lines = file.read().splitlines()

worded_digits = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def get_line_digit(line):
    # returns first number found from line
    return re.search(r"\d+", line).group()

def replace_all_words(line):
    # replace all english numbers with number + english number + number
    for num in worded_digits:
        line = line.replace(num, num + str(worded_digits.index(num)) + num)
    return line

def get_line_values(lines):
    lines_values = []
    
    for line in lines:
        line = replace_all_words(line)
        line_value = get_line_digit(line) + get_line_digit(line[::-1])
        lines_values.append(int(line_value))
    return lines_values

lines_values_total = get_line_values(lines)

print(sum(lines_values_total))