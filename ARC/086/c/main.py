n, k = map(int, input().split())
A = list(map(int, input().split()))
array = {}
ans = 0

for a in A:
    if a in array.keys():
        array[a] += 1
    else:
        array[a] = 1

array = sorted(array.values())

if len(set(A)) > k:
    num = len(array) - k
    for i in range(num):
        ans += array[i]

print(ans)
