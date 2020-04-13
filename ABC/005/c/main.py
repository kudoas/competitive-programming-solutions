t = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

takoyaki_id = -1
cnt = 0
for b in B:
    for i in range(n):
        if A[i] <= b <= A[i] + t and takoyaki_id < i:
            takoyaki_id = i
            cnt += 1
            break

ans = 'yes' if cnt == m else 'no'
print(ans)
