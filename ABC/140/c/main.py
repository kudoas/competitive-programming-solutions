n = int(input())
B = list(map(int, input().split()))

cnt = B[0] + B[-1]

for i in range(0, n-2):
    # if B[i] > B[i+1]:
    #     cnt += B[i+1]
    # else:
    #     cnt += B[i]
    cnt += min(B[i], B[i+1])

print(cnt)
