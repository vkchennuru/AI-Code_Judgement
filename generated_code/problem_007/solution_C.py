import sys

data = list(map(int, sys.stdin.read().split()))
if data:
n = data[0]
nums = data[1:1+n]
print(max(nums))
