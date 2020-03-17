n, x = map(int, input().split())
A = list(map(int, input().split()))
ans = 0

for i in range(n):
    # 2進数で右へシフト、一番右の数が1だったら1を返してリストの値が足される
    ans += ((x >> i) & 1) * A[i]

print(ans)
