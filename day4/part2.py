#!/usr/bin/env python3

def is_valid(r):
  for i in range(0, len(r)):
    for j in range(i + 1, len(r)):
      if sorted(r[i]) == sorted(r[j]):
        return 0
  return 1

rs = []
with open("input.txt") as f:
  for l in f.readlines():
    r = l.split()
    if r:
      rs.append(r)
t = 0
for r in rs:
  t += is_valid(r)
print(t)

