#!/usr/bin/env python3

def main():
  with open("input.txt") as f:
    lines = [line.split(" starts with ") for line in f.read().strip().split("\n")]
  (a, b) = (int(lines[0][1]), int(lines[1][1]))
  count = 0
  for _ in range(40000000):
    a = (a * 16807) % 2147483647
    b = (b * 48271) % 2147483647
    if a & 0xFFFF == b & 0xFFFF:
      count += 1
  print(count)

if __name__ == "__main__":
  main()
