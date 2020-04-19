from collections import Counter

n = int(input())
a = Counter(list(map(int, input().split())))

for i in range(1, n+1):
    print(a[i])
