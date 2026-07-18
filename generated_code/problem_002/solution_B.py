import sys

data = sys.stdin.read().strip()
if data:
r = float(data)
area = 3.14159 * r * r
print(f"{area:.2f}")
