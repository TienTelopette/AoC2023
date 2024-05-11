file = open("C:/Users/ttche/Desktop/AoC2023/Day_1/input.txt","r")
lines = file.readlines()

def get_line_digit(line):
    for char in line:
        if char.isdigit():
            return char

def get_line_values(lines):
    lines_values = []
    for line in lines:
        line_value = get_line_digit(line) + get_line_digit(line[::-1])
        lines_values.append(int(line_value))
    return lines_values


lines_values_total = get_line_values(lines)

print(sum(lines_values_total))