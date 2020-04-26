from collections import Counter


n = int(input())
v = list(map(int, input().split()))
v1 = Counter(v[::2]).most_common(2)
v2 = Counter(v[1::2]).most_common(2)
