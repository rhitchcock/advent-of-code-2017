#!/usr/bin/env python3

import math

def transform(rules, grid):
  size = len(grid)
  n = 3
  if size % 2 == 0:
    n = 2
  # split into subgrids
  subgrids = []
  for row in range(size // n):
    for col in range(size // n):
      subgrid = []
      for i in range(n):
        entry = []
        for j in range(n):
          entry.append(grid[row * n + i][col * n + j])
        subgrid.append("".join(entry))
      subgrids.append("/".join(subgrid))
  # replace subgrids
  for i, subgrid in enumerate(subgrids):
     subgrids[i] = rules[subgrid]
  # join subgrids
  size = int(math.sqrt(len(subgrids)))
  grid = []
  m = len(subgrids[0].split("/"))
  for i in range(size):
    for blah in range(m):
      line = []
      for j in range(size):
        line.append(subgrids[i * size + j].split("/")[blah])
      grid.append("".join(line))
  return grid

def rotate_outside(grid):
  grid = grid.split("/")
  grid = [list(t) for t in zip(*grid[::-1])]
  return "/".join(["".join(row) for row in grid])

def flip(grid):
  return "/".join(reversed(grid.split("/")))

def main():
  grid = [".#.", "..#", "###"]
  with open("input.txt") as f:
    lines = filter(None, f.read().split("\n"))
  rules = {}
  for line in lines:
    (key, value) = line.split(" => ")
    rules[key] = value
    for _ in range(3):
      key = rotate_outside(key)
      rules[key] = value
    key = flip(key)
    rules[key] = value
    for _ in range(3):
      key = rotate_outside(key)
      rules[key] = value
  for _ in range(5):
    grid = transform(rules, grid)
  print(sum(row.count("#") for row in grid))

if __name__ == "__main__":
  main()

