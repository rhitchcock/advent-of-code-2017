#!/usr/bin/env python3

# Rank 134

import string

def run_program(instructions, registers, ip, buff):
  ins = instructions[ip]
  snd = None
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
    if buff:
      registers[ins[1]] = buff.pop(0)
    else:
      ip -= 1
  elif ins[0] == "jgz":
    if (ins[1] not in registers and int(ins[1]) > 0) or (ins[1] in registers and registers[ins[1]] > 0):
      if ins[2] in registers:
        ip += registers[ins[2]] - 1
      else:
        ip += int(ins[2]) - 1
  ip += 1
  return ip, snd

def main():
  registers0 = {c: 0 for c in string.ascii_lowercase}
  registers1 = dict(registers0)
  registers1["p"] = 1
  instructions = []
  with open("input.txt") as f:
    for l in f.read().strip().split("\n"):
      instructions.append(l.split())
  (count, ip0, ip1, buf0, buf1) = (0, 0, 0, [], [])
  while ip0 < len(instructions) or ip1 < len(instructions):
    if ip0 < len(instructions):
      ip0, snd = run_program(instructions, registers0, ip0, buf0)
      if snd:
        buf1.append(snd)
    if ip1 < len(instructions):
      ip1, snd = run_program(instructions, registers1, ip1, buf1)
      if snd:
        count += 1
        buf0.append(snd)
    if instructions[ip0][0] == "rcv" and not buf0 and instructions[ip1][0] == "rcv" and not buf1:
      break
  print(count)

if __name__ == "__main__":
  main()
