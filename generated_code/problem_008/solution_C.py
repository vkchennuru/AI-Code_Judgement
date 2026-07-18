import sys

s = sys.stdin.readline().rstrip("\n")
vowels = set("aeiouAEIOU")
count = sum(1 for ch in s if ch in vowels)
print(count)
