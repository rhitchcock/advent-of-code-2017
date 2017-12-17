#!/usr/bin/env python3

def main():
  with open("input.txt") as f:
    steps = int(f.read().strip())
  spinlock = [0]
  position = 0
  for i in range(1, 2018):
    position = (position + steps) % len(spinlock) + 1
    spinlock.insert(position, i)
  print(spinlock[spinlock.index(2017) + 1])

if __name__ == "__main__":
  main()
