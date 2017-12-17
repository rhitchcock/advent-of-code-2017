#!/usr/bin/env python3

def main():
  firewall = {}
  with open("input.txt") as f:
    for line in f.read().strip().split("\n"):
      parts = line.split(": ")
      firewall[int(parts[0])] = int(parts[1])
  delay = None
  time = 0
  while delay is None:
    delay = time
    for depth in firewall:
      if (delay + depth) % (2 * (firewall[depth] - 1)) == 0:
        delay = None
        break
    time += 1
  print(delay)

if __name__ == "__main__":
  main()
