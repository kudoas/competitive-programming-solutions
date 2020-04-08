from heapq import heapify, heappop, heappush
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
A = list(map(int, input().split()))
heapify(A)

BC = [tuple(map(int, input().split())) for _ in range(m)]
BC.sort(key=lambda x: x[1], reverse=True)

for i in range(m):
    for _ in range(BC[i][0]):
        min_num = heappop(A)
        if min_num < BC[i][1]:
            heappush(A, BC[i][1])
        else:
            heappush(A, min_num)
            break

total = sum(A)
print(total)
