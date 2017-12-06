#!/usr/bin/env python3

rs = []
with open("input.txt") as f:
  for l in f.readlines():
    r = l.split()
    if r:
      rs.append(int(r[0]))
i = 0
n = 0
while i < len(rs):
   if rs[i] >= 3:
     rs[i] -= 1
     i += rs[i] + 1
   else:
     rs[i] += 1
     i += rs[i] - 1
   n += 1
print(n)
