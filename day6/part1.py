#!/usr/bin/env python3

with open("input.txt") as f:
  c = tuple(int(i) for i in f.readline().split())
v = set()
n = 0
while c not in v:
  v.add(c)
  m = max(c)
  i = c.index(m)
  l = list(c)
  l[i] = 0
  while m > 0:
    m -= 1
    i += 1
    l[i % len(l)] += 1
  c = tuple(l)
  n += 1
print(n)
