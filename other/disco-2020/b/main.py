n = int(input())
aa = list(map(int, input().split()))
cnt = 0
total = 0

if sum(aa) % 2 == 1:
    for i in range(n):
        if aa[i] != 1:
            aa[i] -= 1
            cnt += 1
            break

half = sum(aa)//2

if sum(aa[:-1]) < aa[-1]:
    print(aa[-1]-sum(aa[:-2]))
    exit()

for i in range(n):
    total += aa[i]
    if total == half:
        print(0)
        exit()
    if total > half:
        cnt += min(abs(half-total), abs(half-total+aa[i+1]))*2
        break

print(cnt)
