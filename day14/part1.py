#!/usr/bin/env python3

import math

def reverse_sublist(l, current_position, length):
  for i in range(math.floor(length / 2)):
    i1 = (current_position + i) % len(l)
    i2 = (current_position + length - i - 1) % len(l)
    l[i1], l[i2] = l[i2], l[i1]

def knot_hash(string):
  items_len = 256
  items = list(range(items_len))
  lengths = [ord(i) for i in string] + [17, 31, 73, 47, 23]
  current_position = 0
  skip_size = 0
  for _ in range(64):
    for length in lengths:
      if length > items_len:
        continue
      reverse_sublist(items, current_position, length)
      current_position = (current_position + length + skip_size) % items_len
      skip_size += 1
  dense_hash = ""
  for i in range(items_len // 16):
    combined = items[i * 16]
    for j in range(1, 16):
      combined ^= items[i * 16 + j]
    dense_hash += "{:02x}".format(combined)
  return dense_hash

def main():
  with open("input.txt") as f:
    key = f.read().strip()
  num_used = 0
  for i in range(128):
    for j in bin(int(knot_hash(key + "-" + str(i)), 16))[2:].zfill(128):
      if j == "1":
        num_used += 1
  print(num_used)

if __name__ == "__main__":
  main()
