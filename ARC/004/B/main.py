n = int(input())
D = [int(input()) for _ in range(n)]

# n角形成立条件
# 最大の長さのをd_eの長さとすると、それら以外の辺の合計よりも小さければ多角形
# d_e < d_1 + d_2+...+d_N
x = sum(D)
y = max(D)
if x > y+y:
    print(x, 0, sep='\n')
else:
    print(x, y+y-x, sep='\n')
