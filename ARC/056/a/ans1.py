a, b, k, l = map(int, input().split())

# setで買える分は全部買う
# 端数はsetで買うほうがいいか、バラでピッタリ買うかで安い方

set_num = k // l
rem_num = k % l

if rem_num * a >= b:
    price = (set_num + 1) * b
else:
    price = set_num * b + rem_num * a

print(price)
