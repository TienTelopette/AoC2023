import re
import os

path = os.path.join(os.getcwd(), "day-12", "input.txt")
file = open(path)
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