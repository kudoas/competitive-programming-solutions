import bisect

n = int(input())
S = list(map(int, input().split()))  # sorted
q = int(input())
T = list(map(int, input().split()))

cnt = 0
for t in T:
    idx = bisect.bisect_right(S, t)
    if S[idx-1] == t:
        cnt += 1

print(cnt)
