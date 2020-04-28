from collections import defaultdict

s = input()
n = len(s)
MOD = 2019

# for x in s[::-1]:
#     int(x)

dd = defaultdict(int)
dd[0] += 1
prev = 0
for i in reversed(range(n)):
    # お尻から順に数字が取れる
    # これだといちいち参照して間に合わない
    # x = int(s[i:]) % MOD
    prev = (prev + int(s[i])*pow(10, n-i, MOD)) % MOD
    dd[prev] += 1

# print(dd)
ans = sum(v*(v-1)//2 for v in dd.values())
print(ans)

# これだと遅い
