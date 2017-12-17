#!/usr/bin/env python3

def main():
  with open("input.txt") as f:
    steps = int(f.read().strip())
  solution = 0
  position = 0
  for i in range(1, 50000001):
    position = (position + steps) % i + 1
    if position == 1:
      solution = i
  print(solution)

if __name__ == "__main__":
  main()
