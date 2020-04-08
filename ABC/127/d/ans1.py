from heapq import heapify, heappop, heappush
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
A = list(map(int, input().split()))
A.sort(reverse=True)

BC = [tuple(map(int, input().split())) for _ in range(m)]
BC.sort(key=lambda x: x[1], reverse=True)

answer = 0
for b, c in BC:
    for _ in range(b):
        if not A:
            break
        a = A.pop()
        answer += max(a, c)

answer += sum(A)

print(answer)
