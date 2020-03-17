n, m = map(int, input().split())

n = n % 12

short = n/12+(m/60*1/12)
long = m/60

diff = abs(long-short)
ans = 360*min(diff, 1-diff)

print(ans)
