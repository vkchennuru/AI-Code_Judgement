from collections import OrderedDict
import sys

line = sys.stdin.readline().rstrip("\n")
words = line.split()

freq = OrderedDict()
for w in words:
freq[w] = freq.get(w, 0) + 1

for w, c in freq.items():
print(w, c)
