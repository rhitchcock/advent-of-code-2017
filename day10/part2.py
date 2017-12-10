#!/usr/bin/env python3

import math

def reverse_sublist(l, current_position, length):
  for i in range(math.floor(length / 2)):
    i1 = (current_position + i) % len(l)
    i2 = (current_position + length - i - 1) % len(l)
    l[i1], l[i2] = l[i2], l[i1]

def main():
  items_len = 256
  items = list(range(items_len))
  with open("input.txt") as f:
    lengths = [ord(i) for i in f.read().strip()]
  lengths.extend([17, 31, 73, 47, 23])
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
  print(dense_hash)
 
if __name__ == "__main__":
  main()
