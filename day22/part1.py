#!/usr/bin/env python3

import math
from collections import defaultdict

def main():
  with open("input.txt") as f:
    lines = f.readlines()
  size = len(lines)
  grid = defaultdict(bool)
  for row in range(size):
    for col in range(size):
      grid[(col, row)] = lines[row][col] == "#"
  x = size // 2
  y = size // 2
  dx = 0
  dy = -1
  count = 0
  for _ in range(10000):
    if grid[(x, y)]:
      dx, dy = -dy, dx
      grid[(x, y)] = False
    else:
      dx, dy = dy, -dx
      grid[(x, y)] = True
      count += 1
    x, y = x + dx, y + dy
  print(count)

if __name__ == "__main__":
  main()
