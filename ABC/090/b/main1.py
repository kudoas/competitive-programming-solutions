a, b = map(int, input().split())
cnt = 0

for i in range(10):
    for j in range(10):
        for k in range(10):
            c = 10000*i+1000*j+100*k+10*j+i
            if a <= c <= b:
                cnt += 1

print(cnt)
