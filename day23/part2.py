#!/usr/bin/env python3

import argparse

def solve(n):
  with open(n) as f:
    lines = f.read().split("\n")
  registers = {chr(k): 0 for k in range(ord("b"), ord("h") + 1)}
  registers["a"] = 1
  ip = 0
  count = 0
  while ip < len(lines):
    line = lines[ip].split(" ")
    print(ip, line, registers)
    if line[0] == "set":
      if line[2] in registers:
        registers[line[1]] = registers[line[2]]
      else:
        registers[line[1]] = int(line[2])
    elif line[0] == "sub":
      if line[2] in registers:
        registers[line[1]] -= registers[line[2]]
      else:
        registers[line[1]] -= int(line[2])
    elif line[0] == "mul":
      if line[2] in registers:
        registers[line[1]] *= registers[line[2]]
      else:
        registers[line[1]] *= int(line[2])
      count += 1
    elif line[0] == "jnz":
      if line[1] in registers:
        if registers[line[1]] != 0:
          ip += int(line[2]) - 1
      else:
        if int(line[1]) != 0:
          ip += int(line[2]) - 1
    ip += 1
  print(registers["h"])

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("filename")
  args = parser.parse_args()
  solve(args.filename)
