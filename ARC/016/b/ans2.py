n = int(input())
score = [list(input()) for _ in range(n)]
ans = 0

for s in zip(*score):
    long = 0
    for ss in s:
        # 前の値が連続し始めたら1
        # print(s, ss, long)
        if ss == 'x':
            ans += 1
        long ^= ss != 'o' and long
        # 最初の1になった場所をカウント
        if ss == 'o' and not long:
            long ^= 1
            ans += 1

print(ans)
