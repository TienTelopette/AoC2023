import re

file = open("/Users/Tien/Documents/GitHub/AoC2023/Day_12/test_input.txt","r")
data = [line.split(" ") for line in file.read().splitlines()]


'''
?###???????? 	3,2,1
.###???????? 	3,2,1
.###.??????? 	2,1
  .###.##.???? 	1   
  .###.##.#...
  .###.##..#..
  .###.##...#.
  .###.##....#	
.###..##.???    1
  .###..##.#..
  .###..##..#.
  .###..##...#
.###...##.??	1
  .###...##.#.
  .###...##..#
.###....##??	1
  .###....##.#
  
.??..??...?##. 	1,1,3
.#...??...?##.	1,3
.#...#....?##.  3
  .#...#....###.
.#....#...?##.	3
  .#....#...###.
..#..??...?##.	1,3
  ..#..#....?##	3
  ..#..#....###.
..#...#...?##.	3
  ..#...#...###.
  '''

print(re.findall(r"[\W]",data[0][0]))