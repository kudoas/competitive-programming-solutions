n, q = map(int, input().split())
s = input()
cum_sum = [0] * (n+1)

# 空文字からは見ない
for i in range(n):
    if s[:i+1][-2:] == 'AC':
        cum_sum[i+1] += 1
    cum_sum[i+1] += cum_sum[i]

for _ in range(q):
    l, r = map(int, input().split())
    print(cum_sum[r]-cum_sum[l])
