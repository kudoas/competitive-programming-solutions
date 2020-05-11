n, k = map(int, input().split())
se = set()
for _ in range(k):
    d = int(input())
    a = list(map(int, input().split()))
    for aa in a:
        se.add(aa)

print(n-len(se))
