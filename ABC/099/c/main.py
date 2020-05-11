# 残り必要な金額から貪欲に払える最大値を払っていったら間違い
# eg.N=30 貪欲に引いたら-9,-9,-9,-1,-1,-1で６回になるけど、最適解は-9,-9,-6,-6とかの４回。
# import copy

# n = int(input())
# expo6 = [6**i for i in range(1, 10)]
# expo9 = [9**i for i in range(1, 10)]
# expo = sorted(set(expo9+expo6), reverse=True)

# _max = copy.copy(n)
# cnt = 0
# while _max >= 6:
#     for e in expo:
#         if _max >= e:
#             _max -= e
#             cnt += 1
#             break

# print(cnt+_max)

n = int(input())
ans = n
for i in range(n + 1):
    cc = 0
    t = i
    while t > 0:
        cc += t % 6
        t //= 6
    t = n - i
    while t > 0:
        cc += t % 9
        t //= 9
    ans = min(ans, cc)
print(ans)
