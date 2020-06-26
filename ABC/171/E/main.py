n = int(input())
A = list(map(int, input().split()))
total_xor = A[0]
for i in range(1, n):
    total_xor ^= A[i]
ans = []
_total_xor = int(total_xor)
for i in range(n):
    total_xor = _total_xor ^ A[i]
    ans.append(total_xor)
print(*ans)
