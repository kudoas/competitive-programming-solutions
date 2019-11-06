import bisect
import sys

input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))
l.sort()
cnt = 0

for i in range(0, n-2):
    for j in range(i+1, n-1):
        cnt += bisect.bisect_left(l, l[i] + l[j]) - j-1
        # print(i, j, l[i], l[j], t, idx, cnt)

print(cnt)
