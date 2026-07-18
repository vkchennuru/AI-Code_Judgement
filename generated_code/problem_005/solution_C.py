import sys

data = sys.stdin.read().strip()
if data:
n = int(data)
fact = 1
for i in range(2, n + 1):
fact *= i
print(fact)
