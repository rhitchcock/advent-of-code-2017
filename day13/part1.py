#!/usr/bin/env python3

def main():
  firewall = {}
  with open("input.txt") as f:
    for line in f.read().strip().split("\n"):
      parts = line.split(": ")
      # firewall[depth] = [range, position, direction]
      firewall[int(parts[0])] = [int(parts[1]), 0, -1]
  total_severity = 0
  for step in range(max(firewall.keys()) + 1):
    layer = firewall.get(step)
    if layer and layer[1] == 0:
      total_severity += step * layer[0]
    for layer in firewall.values():
      if layer[1] == 0 or layer[1] == layer[0] - 1:
        layer[2] *= -1
      layer[1] += layer[2]
  print(total_severity)

if __name__ == "__main__":
  main()
