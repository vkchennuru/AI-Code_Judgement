import sys

data = sys.stdin.read().split()
a = int(data[0])
b = int(data[1])
print(a if a >= b else b)
