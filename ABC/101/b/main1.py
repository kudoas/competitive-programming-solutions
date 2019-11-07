n = int(input())
s = 0

# n=0で処理が止まる
while n:
    q, r = divmod(n, 10)
    n = q
    print(n)
    s += r

print('Yes' if n % s == 0 else 'No')
