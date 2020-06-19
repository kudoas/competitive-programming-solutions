from collections import Counter


L = Counter(map(int, input().split())).most_common()
print(L[0][0] if len(L) == 1 else L[1][0])
