n = int(input())
s = input()

start = 'b'

# n = 1の時に注意
i = 0
while n >= len(start):
    if start == s:
        print(i)
        exit()
    i += 1
    if i % 3 == 1:
        start = 'a' + start + 'c'
    if i % 3 == 2:
        start = 'c' + start + 'a'
    if i % 3 == 0:
        start = 'b' + start + 'b'

print(-1)
