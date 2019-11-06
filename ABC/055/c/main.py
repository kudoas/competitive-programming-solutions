n, m = map(int, input().split())

cnt = 0

if n*2 <= m:
    cnt += n
    m = m-(n*2)
    cnt += m//4
else:
    cnt += m//2

print(cnt)
