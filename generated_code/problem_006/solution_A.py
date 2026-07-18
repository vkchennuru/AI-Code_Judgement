import sys
import math

def is_prime(n):
if n < 2:
return False
if n == 2:
return True
if n % 2 == 0:
return False
r = int(math.isqrt(n))
i = 3
while i <= r:
if n % i == 0:
return False
i += 2
return True

data = sys.stdin.read().strip()
n = int(data)
print("Prime" if is_prime(n) else "Not Prime")
