# s = input().split('+')
# c = 0

# for i in range(len(s)):
#     ls = [s for s in s[i]]
#     if '0' not in ls:
#         c += 1

# print(c)

# map関数はiterable
S = map(str, input().split('+'))
c = 0

for s in S:
    if '0' not in s:
        c += 1

print(c)
