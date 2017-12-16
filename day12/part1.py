#!/usr/bin/env python3

from queue import Queue

def main():
  adjacency = {}
  with open("input.txt") as f:
    for line in f.read().strip().split("\n"):
      parts = line.split(" <-> ")
      adjacency[parts[0]] = parts[1].split(", ")
  visited = set()
  queue = Queue()
  queue.put("0")
  while not queue.empty():
    program = queue.get()
    for adjacent in adjacency[program]:
      if adjacent not in visited:
        queue.put(adjacent)
    visited.add(program)
  print(len(visited))

if __name__ == "__main__":
  main()
