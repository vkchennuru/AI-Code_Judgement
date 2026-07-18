import sys
import math

def is_prime(n):
if n <= 1:
return False
if n <= 3:
return True
if n % 2 == 0 or n % 3 == 0:
return False
limit = int(math.isqrt(n))
i = 5
while i <= limit:
if n % i == 0 or n % (i + 2) == 0:
return False
i += 6
return True

data = sys.stdin.read().strip()
n = int(data)
print("Prime" if is_prime(n) else "Not Prime")
