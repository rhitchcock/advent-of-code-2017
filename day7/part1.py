#!/usr/bin/env python3

d = {}
with open("input.txt") as f:
  for (l1, l2) in filter(lambda l: len(l) > 1, (l.replace("\n", "").split(" -> ") for l in f.readlines())):
    p = l1.split()[0]
    for c in l2.split(", "):
      d[c] = p
c = next(iter(d.keys()))
p = d.get(c)
while p is not None:
  p = d.get(c)
  if p is not None:
    c = p
print(c)
