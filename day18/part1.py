#!/usr/bin/env python3

# Rank 142

import string

def main():
  registers = {c: 0 for c in string.ascii_lowercase}
  instructions = []
  with open("input.txt") as f:
    for l in f.read().strip().split("\n"):
      instructions.append(l.split())
  ip = 0
  snd = 0
  while ip < len(instructions):
    ins = instructions[ip]
    if ins[0] == "snd":
      if ins[1] in registers:
        snd = registers[ins[1]]
      else:
        snd = int(ins[1])
    elif ins[0] == "set":
      if ins[2] in registers:
        registers[ins[1]] = registers[ins[2]]
      else:
        registers[ins[1]] = int(ins[2])
    elif ins[0] == "add":
      if ins[2] in registers:
        registers[ins[1]] += registers[ins[2]]
      else:
        registers[ins[1]] += int(ins[2])
    elif ins[0] == "mul":
      if ins[2] in registers:
        registers[ins[1]] *= registers[ins[2]]
      else:
        registers[ins[1]] *= int(ins[2])
    elif ins[0] == "mod":
      if ins[2] in registers:
        registers[ins[1]] %= registers[ins[2]]
      else:
        registers[ins[1]] %= int(ins[2])
    elif ins[0] == "rcv":
      if (ins[1] not in registers and ins[1] != 0) or (ins[1] in registers and registers[ins[1]] != 0):
        print(snd)
        return
    elif ins[0] == "jgz":
      if (ins[1] not in registers and registers[ins[1]] > 0) or (ins[1] in registers and registers[ins[1]] > 0):
        ip += int(ins[2]) - 1
    ip += 1

if __name__ == "__main__":
  main()
