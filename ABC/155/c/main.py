import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())
S = [input().rstrip() for _ in range(n)]

c = Counter(S)
max = max(c.values())

words = [k for k, v in c.items() if max == v]
words.sort()

print(*words, sep='\n')
