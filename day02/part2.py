#!/usr/bin/env python3

def divide(r):
  for i in range(0, len(r)):
    for j in range(i + 1, len(r)):
      if r[i] % r[j] == 0:
        return int(r[i] / r[j])
      elif r[j] % r[i] == 0:
        return int(r[j] / r[i])

c = 0
with open("input.txt") as f:
  for l in f.readlines():
    r = [int(i) for i in l.split()]
    if r:
      c += divide(r)
print(c)
