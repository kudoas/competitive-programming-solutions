n = int(input())
a = list(map(int, input().split()))

ans = [0] * (int(1e5)+2)
for i in range(n):
    ans[a[i]-1] += 1
    ans[a[i]] += 1
    ans[a[i]+1] += 1

print(max(ans))
