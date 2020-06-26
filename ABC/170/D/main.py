n = int(input())
A = list(map(int, input().split()))
A.sort()

is_valid = [True] * n
for i in range(n-1):
    if not is_valid[i]:
        continue
    for j in range(i+1, n):
        if not is_valid[j]:
            continue
        if A[j] % A[i] == 0:
            is_valid[j] = False

for i in range(1, n):
    if A[0] % A[j] == 0:
        is_valid[0] = False
        break

print(sum(is_valid))
