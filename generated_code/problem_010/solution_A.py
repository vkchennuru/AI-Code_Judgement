import sys

sys.setrecursionlimit(10000)

data = sys.stdin.read().strip()
n = int(data) if data else 0

def fib(x):
if x <= 1:
return x
return fib(x - 1) + fib(x - 2)

print(fib(n))
