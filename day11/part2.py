#!/usr/bin/env python3

import math

def main():
  with open("input.txt") as f:
    directions = f.read().strip().split(",")
  n = 0
  ne = 0
  nw = 0
  furthest_distance = 0
  for direction in directions:
    if direction == "s":
      n -= 1
    elif direction == "n":
      n += 1
    elif direction == "ne":
      ne += 1
    elif direction == "se":
      nw -= 1
    elif direction == "sw":
      ne -= 1
    elif direction == "nw":
      nw += 1
    furthest_distance = max(furthest_distance, abs(n) + abs(ne) + max(0, abs(nw) - abs(ne)))
  print(furthest_distance)

if __name__ == "__main__":
  main()
