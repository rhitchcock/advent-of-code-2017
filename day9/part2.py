#!/usr/bin/env python3

def main():
  with open("input.txt") as f:
    data = f.read()
  garbage_count = 0
  garbage = False
  i = 0
  end = len(data)
  while i < end:
    if garbage:
      if data[i] == ">":
        garbage = False
      elif data[i] == "!":
        i += 1
      else:
        garbage_count += 1
    elif data[i] == "<":
      garbage = True
    i += 1
  print(garbage_count)

if __name__ == "__main__":
  main()
