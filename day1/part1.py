#!/usr/bin/env python3

t = 0
with open("input.txt") as f:
  c = f.readline().split()[0]
  for i in range(0, len(c)):
    if c[i] == c[(i + 1) % len(c)]:
      t += int(c[i])
print(t)

