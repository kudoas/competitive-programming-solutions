N = int(input())
arr = input().split()

answer = arr[::2][::-1]+arr[1::2]
if not N & 1:
    answer = answer[::-1]

print(*answer)
