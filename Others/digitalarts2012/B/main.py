C = list(input())
alp = '?abcdefghijklmnopqrstuvwxyz'
nums = [alp.index(c) for c in C]
# a: 1 or z: 20
if C == ['a'] or C == ["z"]*20:
    print('NO')
    exit()
ans = []
total = sum(nums)
