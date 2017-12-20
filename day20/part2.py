#!/usr/bin/env python3

import re
import collections

def main():
  particles = []
  with open("input.txt") as f:
    data = f.read()
  r = re.compile(r"p=<(-?\d+),(-?\d+),(-?\d+)>, v=<(-?\d+),(-?\d+),(-?\d+)>, a=<(-?\d+),(-?\d+),(-?\d+)>")
  for m in filter(None, (r.match(l) for l in data.split("\n"))):
    p = [int(m.group(1)), int(m.group(2)), int(m.group(3))]
    v = [int(m.group(4)), int(m.group(5)), int(m.group(6))]
    a = [int(m.group(7)), int(m.group(8)), int(m.group(9))]
    particles.append([p, v, a])
  for _ in range(10000):
    for particle in particles:
      particle[1][0] += particle[2][0]
      particle[1][1] += particle[2][1]
      particle[1][2] += particle[2][2]
      particle[0][0] += particle[1][0]
      particle[0][1] += particle[1][1]
      particle[0][2] += particle[1][2]
    counter = collections.Counter(tuple(particle[0]) for particle in particles)
    duplicates = set()
    for key, value in counter.items():
      if value > 1:
        duplicates.add(key)
    particles = [particle for particle in particles if tuple(particle[0]) not in duplicates]
  print(len(particles))

if __name__ == "__main__":
  main()
