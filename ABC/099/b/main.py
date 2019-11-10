a, b = map(int, input().split())
cnt = 0

for i in range(b-a):
    cnt += i

print(cnt-a)
