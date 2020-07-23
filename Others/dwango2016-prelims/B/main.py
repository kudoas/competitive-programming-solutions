N = int(input())
*K, = map(int, input().split())
ans = [0]*N
ans[0] = K[0]
ans[-1] = K[-1]
i = 0
while i+2 < N:
    ans[i+1] = min(K[i], K[i+1])
    i += 1
print(*ans)
