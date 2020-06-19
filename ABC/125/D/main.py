n = int(input())
A = list(map(int, input().split()))
minus = 0
for i in range(n):
    if A[i] < 0:
        minus += 1
        A[i] *= -1
if minus % 2 == 0:
    ans = sum(A)
else:
    ans = sum(A) - min(A)*2
print(ans)
