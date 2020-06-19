from collections import deque

n = int(input())
A = list(map(int, input().split()))
A.sort()
if A[0] == 1:
    print(0)
    exit()
