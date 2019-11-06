n, m = map(int, input().split())
ls = [int(input()) for _ in range(n)]
# ls.sort()

# m -= sum(ls)
# cnt = n

# while True:
#     if m >= ls[0]:
#         m -= ls[0]
#         cnt += 1
#     else:
#         break

# print(cnt)

print(n+((m-sum(ls))//min(ls)))
