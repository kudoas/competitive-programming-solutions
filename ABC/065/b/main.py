n = int(input())
A = [int(input()) for _ in range(n)]

next = 0
ans = 0
while ans <= n:
    ans += 1
    if A[next] == 2:
        print(ans)
        exit()
    next = A[next]-1

print(-1)
