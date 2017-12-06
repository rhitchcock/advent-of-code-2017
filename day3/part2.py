#!/usr/bin/env python3

def get_larger(n):
  m = {(0, 0): 1}
  s = 3
  x = 0
  y = 0
  while True:
    x += 1
    y -= 1
    for j in range(0, (s - 1) * 4):
      if j < s - 1:
        y += 1
      elif j < (s - 1) * 2:
        x -= 1
      elif j < (s - 1) * 3:
        y -= 1
      else:
        x += 1
      d = (
          m.get((x - 1, y - 1), 0) +
          m.get((x,     y - 1), 0) +
          m.get((x + 1, y - 1), 0) +
          m.get((x - 1, y    ), 0) +
          m.get((x + 1, y    ), 0) +
          m.get((x - 1, y + 1), 0) +
          m.get((x    , y + 1), 0) +
          m.get((x + 1, y + 1), 0)
        )
      if d > n:
        return d
      else:
        m[(x, y)] = d
    s += 2

with open("input.txt") as f:
  print(get_larger(int(f.readline().split()[0])))
