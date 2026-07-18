import sys

data = list(map(int, sys.stdin.read().split()))
n = data[0]
arr = data[1:1 + n]
print(max(arr))
