n, k = map(int, input().split())
d = set(map(int, input().split()))
d ^= {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}

while True:
    if d >= set(map(int, list(str(n)))):
        print(n)
        break
    n += 1
