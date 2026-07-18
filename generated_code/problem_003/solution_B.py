import sys

data = sys.stdin.read().split()
a, b = map(int, data[:2])
print(a if a >= b else b)
