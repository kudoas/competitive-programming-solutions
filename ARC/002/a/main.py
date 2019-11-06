y = int(input())
print("YES" if y % 4 == 0 and y % 100 != 0 or y % 400 == 0 else "NO")

# if y % 400 == 0:
#     print('YES')
#     exit()
# elif y % 100 == 0:
#     print('NO')
#     exit()
# elif y % 4 == 0:
#     print('YES')
#     exit()
# else:
#     print('NO')
