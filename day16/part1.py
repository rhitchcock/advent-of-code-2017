#!/usr/bin/env python3

def main():
  programs = "abcdefghijklmnop"
  with open("input.txt") as f:
    for line in f.read().strip().split(","):
      if line.startswith("s"):
        num = int(line[1:])
        programs = programs[-num:] + programs[:-num]
      elif line.startswith("x"):
        (first, second) = map(int, line[1:].split("/"))
        programs = list(programs)
        programs[first], programs[second] = programs[second], programs[first]
        programs = "".join(programs)
      elif line.startswith("p"):
        (first, second) = map(programs.index, line[1:].split("/"))
        programs = list(programs)
        programs[first], programs[second] = programs[second], programs[first]
        programs = "".join(programs)
  print(programs)

if __name__ == "__main__":
  main()
