n = int(input())
a = list(map(int, input().split()))
start = sum(a)//2-sum(a[1::2])
ans = [start*2]

for i in range(n-1):
    ans.append((a[i] - start)*2)
    start = a[i] - start

print(*ans)
