#!/usr/bin/env python3

# TODO: Clean up the code.

import collections

p = {}
c = {}
w = {}
t = True

def get_weight(root):
  global c,w,t
  children = c.get(root, list())
  child_weights = {}
  for child in children:
    child_weights[child] = get_weight(child)
  counter = collections.Counter(child_weights.values())
  if t and len(counter) > 1:
    t = False
    most_common = counter.most_common(1)[0][0]
    for child in children:
      if child_weights[child] != most_common:
        print(w[child] + most_common - child_weights[child])
  return w[root] + sum(child_weights.values())

with open("input.txt") as f:
  for l in (l.replace("\n", "").split(" -> ") for l in f.readlines()):
    p1 = l[0].split()
    if p1:
      parent = p1[0]
      w[parent] = int(p1[1][1:-1])
      if len(l) > 1:
        children = l[1].split(", ")
        for child in children:
          p[child] = parent
        c[parent] = children
child = next(iter(p.keys()))
parent = p.get(child)
while parent is not None:
  parent = p.get(child)
  if parent is not None:
    child = parent
get_weight(child)
