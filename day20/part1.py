#!/usr/bin/env python3

import re

def main():
  particles = []
  with open("input.txt") as f:
    data = f.read()
  r = re.compile(r"p=<(-?\d+),(-?\d+),(-?\d+)>, v=<(-?\d+),(-?\d+),(-?\d+)>, a=<(-?\d+),(-?\d+),(-?\d+)>")
  i = 0
  for m in filter(None, (r.match(l) for l in data.split("\n"))):
    p = [int(m.group(1)), int(m.group(2)), int(m.group(3))]
    v = [int(m.group(4)), int(m.group(5)), int(m.group(6))]
    a = [int(m.group(7)), int(m.group(8)), int(m.group(9))]
    particles.append([p, v, a, i])
    i += 1
  if particles:
    particles = sorted(particles, key=lambda particle:
      (
        abs(particle[2][0]) + abs(particle[2][1]) + abs(particle[2][2]),
        abs(particle[1][0]) + abs(particle[1][1]) + abs(particle[1][2]),
        abs(particle[0][0]) + abs(particle[0][1]) + abs(particle[0][2])
      )
    )
    print(particles[0][3])

if __name__ == "__main__":
  main()
