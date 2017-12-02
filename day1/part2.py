#!/usr/bin/env python3

total = 0
with open("input.txt") as f:
  code = f.readline().split()[0]
  for i in range(0, len(code)):
    if code[i] == code[int(i + len(code) / 2) % len(code)]:
      total += int(code[i])
print(total)

