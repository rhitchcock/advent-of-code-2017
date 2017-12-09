#!/usr/bin/env python3

def main():
  with open("input.txt") as f:
    data = f.read()
  depth = 0
  score = 0
  garbage = False
  i = 0
  end = len(data)
  while i < end:
    if garbage:
      if data[i] == ">":
        garbage = False
      elif data[i] == "!":
        i += 1
    elif data[i] == "{":
      depth += 1
    elif data[i] == "}":
      score += depth
      depth -= 1
    elif data[i] == "<":
      garbage = True
    i += 1
  print(score)

if __name__ == "__main__":
  main()
