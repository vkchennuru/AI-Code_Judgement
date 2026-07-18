import sys

sentence = sys.stdin.readline().strip()
words = sentence.split()

freq = {}
order = []

for word in words:
if word not in freq:
freq[word] = 1
order.append(word)
else:
freq[word] += 1

for word in order:
print(word, freq[word])
