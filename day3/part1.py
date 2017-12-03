#!/usr/bin/env python3

with open("input.txt") as f:
  n = int(f.readline().split()[0])
i = 1
s = 1
while i < n:
  i += s * 4 + 4
  s += 2
a = int(s / 2)
if s == 1:
  print(0)
elif (i - n + a) % (s - 1) > a - 1:
  print(a + (n - (i - (s - 2) * 4 - 4) + a) % (s - 1))
else:
  print(a + (i - n + a) % (s - 1))

