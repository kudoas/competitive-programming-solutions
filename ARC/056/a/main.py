a, b, k, l = map(int, input().split())
max_num = k + l
price = float('inf')

# TLE
for i in range(k, max_num+1):
    num = i % l
    set_num = i // l
    price = min(price, a*num+b*set_num)

print(price)
