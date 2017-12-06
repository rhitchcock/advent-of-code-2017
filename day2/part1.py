#!/usr/bin/env python3

c = 0
with open("input.txt") as f:
  for l in f.readlines():
    r = [int(i) for i in l.split()]
    if r:
      c += max(r) - min(r)
print(c)
