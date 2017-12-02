#!/usr/bin/env python3

checksum = 0
with open("input.txt") as f:
  for l in f.readlines():
    row = [int(i) for i in l.split()]
    checksum += max(row) - min(row)
print(checksum)

