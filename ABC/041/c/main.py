from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))
d = defaultdict(int)

for i in range(n):
    d[i+1] = a[i]

d = sorted(d.items(), key=lambda x: x[1], reverse=True)

for stundent in d:
    print(stundent[0])
