# x, y = input().split()
# ls = ['A', 'B', 'C', 'D', 'E', 'F']

# x = ls.index(x)
# y = ls.index(y)

# if x < y:
#     print('<')
# elif x == y:
#     print('=')
# else:
#     print('>')

# そもそもこれで行ける
a, b = input().split()
if a > b:
    print('>')
elif a == b:
    print('=')
else:
    print('<')
