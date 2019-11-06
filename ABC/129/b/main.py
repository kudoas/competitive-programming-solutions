n = int(input())
W = list(map(int, input().split()))

ls = []
cnt = 0
total = sum(W)

for i in range(n):
    cnt += W[i]
    ls.append(abs(cnt-abs(total-cnt)))

print(min(ls))
