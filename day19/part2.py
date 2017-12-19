#!/usr/bin/env python3

def main():
  grid = {}
  start_col = None
  with open("input.txt") as f:
    row = 0
    for l in f.read().split("\n"):
      for col in range(len(l)):
        if not start_col and l[col] == "|":
          start_col = col
        grid[(col, row)] = l[col]
      row += 1
  x = start_col
  y = 0
  velocity = (0, 1)
  count = 0
  while (x, y) in grid:
    c = grid[(x, y)]
    if c == " ":
      break
    elif c == "+":
      if velocity != (0, -1) and (x, y + 1) in grid and grid[(x, y + 1)] != " ":
        velocity = (0, 1)
      elif velocity != (0, 1) and (x, y - 1) in grid and grid[(x, y - 1)] != " ":
        velocity = (0, -1)
      elif velocity != (-1, 0) and (x + 1, y) in grid and grid[(x + 1, y)] != " ":
        velocity = (1, 0)
      elif velocity != (1, 0) and (x - 1, y) in grid and grid[(x - 1, y)] != " ":
        velocity = (-1, 0)
      else:
        break
    x += velocity[0]
    y += velocity[1]
    count += 1
  print(count)

if __name__ == "__main__":
  main()
