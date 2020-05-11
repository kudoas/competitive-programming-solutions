# n, x = map(int, input().split())
# A = list(map(int, input().split()))
# prev = 0
# ans = 0
# for a in A:
#     eat = max(0, prev+a-x)
#     prev = a - eat
#     ans += eat

# print(ans)

# n, x = map(int, input().split())
# A = list(map(int, input().split()))
# ans = 0
# for i in range(1, n):
#     if A[i-1]+A[i] <= x:
#         continue
#     eat = A[i-1]+A[i] - x
#     ans += eat
#     A[i] = max(0, A[i]-eat)

# print(A, ans)

n, x = map(int, input().split())
A = list(map(int, input().split()))
ans = 0
for i in range(n):
    if i == 0:
        if A[i] <= x:
            continue
        eat = A[i] - x
        ans += eat
        A[i] = A[i] - eat
        continue
    if A[i-1]+A[i] <= x:
        continue
    eat = A[i-1] + A[i] - x
    ans += eat
    A[i] = A[i] - eat

print(ans)
