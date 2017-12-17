#!/usr/bin/env python3

def main():
  programs = "abcdefghijklmnop"
  with open("input.txt") as f:
    dance_moves = f.read().strip().split(",")
  visited = set()
  i = 1000000000
  while i > 0:
    visited.add(programs)
    for dance_move in dance_moves:
      if dance_move.startswith("s"):
        num = int(dance_move[1:])
        programs = programs[-num:] + programs[:-num]
      elif dance_move.startswith("x"):
        (first, second) = map(int, dance_move[1:].split("/"))
        programs = list(programs)
        programs[first], programs[second] = programs[second], programs[first]
        programs = "".join(programs)
      elif dance_move.startswith("p"):
        (first, second) = map(programs.index, dance_move[1:].split("/"))
        programs = list(programs)
        programs[first], programs[second] = programs[second], programs[first]
        programs = "".join(programs)
    i -= 1
    if programs in visited:
      i = 1000000000 % (1000000000 - i)
  print(programs)

if __name__ == "__main__":
  main()
