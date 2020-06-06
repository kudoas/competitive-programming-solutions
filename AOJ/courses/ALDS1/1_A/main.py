n = int(input())
A = list(map(int, input().split()))

# i：未ソートの先頭のindex
for i in range(n):
    # v：未ソートの先頭の配列の数
    v = A[i]
    # j：ソート済みの配列からvを差し込む位置を探すループ変数
    j = i - 1
    while j >= 0 and A[j] > v:
        A[j+1] = A[j]
        j -= 1
    A[j+1] = v
    print(*A)
