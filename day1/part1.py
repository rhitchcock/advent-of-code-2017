import sys

if __name__ == "__main__":
  if len(sys.argv) < 2:
    print("Usage: " + sys.argv[0] + " <code>")
  else:
    code = sys.argv[1]
    total = 0
    for i in range(0, len(code)):
      if code[i] == code[(i + 1) % len(code)]:
        total += int(code[i])
    print(total)

