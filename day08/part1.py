#!/usr/bin/env python3

import collections
import operator

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
(_, largest_value) = max(iter(registers.items()), key=operator.itemgetter(1))
print(largest_value)
