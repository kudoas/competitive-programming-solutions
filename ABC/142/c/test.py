n = int(input())
a = list(map(int, input().split()))

ans = [0]*n

for i, item in enumerate(a):
    ans[item-1] = i+1

print(*ans)
