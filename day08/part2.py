#!/usr/bin/env python3

import collections
import operator

largest_value_ever = None
registers = collections.defaultdict(int)
with open("input.txt") as f:
  for parts in filter(None, (line.split() for line in f.readlines())):
    register_to_modify = parts[0]
    sign = 1 if parts[1] == "inc" else -1
    amount = int(parts[2])
    register_condition = parts[4]
    conditional = parts[5]
    value = int(parts[6])
    if (
        (conditional == ">" and registers[register_condition] > value)
        or (conditional == "<" and registers[register_condition] < value)
        or (conditional == ">=" and registers[register_condition] >= value)
        or (conditional == "==" and registers[register_condition] == value)
        or (conditional == "<=" and registers[register_condition] <= value)
        or (conditional == "!=" and registers[register_condition] != value)
      ):
      registers[register_to_modify] += sign * amount
      largest_value_ever = max(registers[register_to_modify], largest_value_ever) if largest_value_ever is not None else registers[register_to_modify]
print(largest_value_ever)
