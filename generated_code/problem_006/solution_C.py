import sys
import math

def is_prime(n):
if n < 2:
return False
if n == 2:
return True
if n % 2 == 0:
return False
limit = int(math.isqrt(n))
for i in range(3, limit + 1, 2):
if n % i == 0:
return False
return True

data = sys.stdin.read().strip()
n = int(data)
print("Prime" if is_prime(n) else "Not Prime")
