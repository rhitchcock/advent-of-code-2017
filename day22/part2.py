#!/usr/bin/env python3

import argparse
import math
import collections

def solve(input_filename):
  with open(input_filename) as f:
    lines = f.readlines()
  size = len(lines)
  grid = collections.defaultdict(lambda: ".")
  for row in range(size):
    for col in range(size):
      grid[(col, row)] = lines[row][col]
  x = size // 2
  y = size // 2
  dx = 0
  dy = -1
  count = 0
  for _ in range(10000000):
    if grid[(x, y)] == "#":
      dx, dy = -dy, dx
      grid[(x, y)] = "F"
    elif grid[(x, y)] == "W":
      grid[(x, y)] = "#"
      count += 1
    elif grid[(x, y)] == "F":
      dx, dy = -dx, -dy
      grid[(x, y)] = "."
    else:
      dx, dy = dy, -dx
      grid[(x, y)] = "W"
    x, y = x + dx, y + dy
  print(count)

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("input_filename")
  args = parser.parse_args()
  solve(args.input_filename)
