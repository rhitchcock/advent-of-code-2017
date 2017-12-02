#!/usr/bin/env python3

def divide(row):
  for i in range(0, len(row)):
    for j in range(i + 1, len(row)):
      if row[i] % row[j] == 0:
        return row[i] / row[j]
      elif row[j] % row[i] == 0:
        return row[j] / row[i]

checksum = 0
with open("input.txt") as f:
  for l in f.readlines():
    checksum += divide([int(i) for i in l.split()])
print(checksum)

