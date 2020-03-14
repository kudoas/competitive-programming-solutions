# dequeを使う解放
from collections import deque

n = int(input())
A = list(map(int, input().split()))
deq = deque([])

for i in range(1, n+1):
    if i % 2 == 1:
        deq.append(A[i-1])
    else:
        deq.appendleft(A[i-1])

if n % 2 == 0:
    print(*deq)
else:
    print(*reversed(list(deq)))
