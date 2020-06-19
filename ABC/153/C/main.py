n, k = map(int, input().split())
H = list(map(int, input().split()))
H.sort(reverse=True)
if n <= k:
    print(0)
    exit()
print(sum(H[k:]))
