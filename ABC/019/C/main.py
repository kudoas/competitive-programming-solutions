# n = int(input())
# A = list(map(int, input().split()))


# def half_num(n):
#     if n % 2:
#         return n
#     return half_num(n//2)


# se = set()
# for a in A:
#     se.add(half_num(a))
# print(len(se))

n = int(input())
A = list(map(int, input().split()))
se = set()
for a in A:
    while a % 2 == 0:
        a //= 2
    se |= {a}
print(len(se))
