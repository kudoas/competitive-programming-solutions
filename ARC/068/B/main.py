from collections import Counter

n = int(input())
A = list(map(int, input().split()))
A.sort()
_max = A[-1]
_min = A[0]
C = Counter(A)
odd = 0
even = 0
for v in C.values():
    if v % 2:
        odd += 1
    else:
        even += 1
ans = odd + (even//2)*2
print(ans)
