n = int(input())
L = list(map(int, input().split()))
L.sort(reverse=True)

print('Yes' if L[0] < sum(L)-L[0] else 'No')
