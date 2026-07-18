import sys

s = sys.stdin.readline().rstrip("\n")
vowels = set("aeiouAEIOU")
count = sum(1 for c in s if c in vowels)
print(count)
