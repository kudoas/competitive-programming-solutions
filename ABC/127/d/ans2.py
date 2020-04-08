from heapq import heapify, heappop, heappush
import heapq
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
A = list(map(int, input().split()))

BC = [tuple(map(int, input().split())) for _ in range(m)]

for b, c in BC:
    for _ in range(b):
        A.append(c)


def _heappush_max(heap, item):
    heap.append(item)
    heapq._siftdown_max(heap, 0, len(heap)-1)


def _heappop_max(heap):
    lastelt = heap.pop()
    if heap:
        returnitem = heap[0]
        heap[0] = lastelt
        heapq._siftup_max(heap, 0)
        return returnitem
    return lastelt


answer = 0
for _ in range(n):
    answer += _heappop_max(A)

print(answer)
