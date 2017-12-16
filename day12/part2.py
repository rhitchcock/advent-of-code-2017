#!/usr/bin/env python3

from queue import Queue

def main():
  adjacency = {}
  with open("input.txt") as f:
    for line in f.read().strip().split("\n"):
      parts = line.split(" <-> ")
      adjacency[parts[0]] = parts[1].split(", ")
  groups = []
  not_visited = set(adjacency.keys())
  while len(not_visited) > 0:
    visited = set()
    queue = Queue()
    queue.put(not_visited.pop())
    while not queue.empty():
      program = queue.get()
      for adjacent in adjacency[program]:
        if adjacent not in visited:
          queue.put(adjacent)
      visited.add(program)
    not_visited = not_visited - visited
    groups.append(visited)
  print(len(groups))

if __name__ == "__main__":
  main()
