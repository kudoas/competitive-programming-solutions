n, k = map(int, input().split())
R = list(map(int, input().split()))
R.sort(reverse=True)
videos = R[:k][::-1]
ans = 0
for i in range(k):
    ans = (videos[i] + ans)/2
print(ans)
