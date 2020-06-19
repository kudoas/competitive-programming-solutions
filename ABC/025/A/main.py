from itertools import product

s = list(input())
n = int(input())
words = []
for s1, s2 in product(s, repeat=2):
    words.append(s1+s2)
print(words[n-1])
