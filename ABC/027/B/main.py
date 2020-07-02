n = int(input())
A = list(map(int, input().split()))
if sum(A) % n:
    print(-1)
    exit()
ave = sum(A)/n
A += [-1]
total = 0
cnt = 0
ans = 0
i = 0
p = 0
while A[i] != -1:
    total += A[i]
    if total/(i+1-p) == ave:
        p = i+1
        ans += cnt
        cnt = 0
        total = 0
    else:
        cnt += 1
    i += 1
print(ans)
