n = int(input())
A = list(map(int, input().split()))
cnt = 0
for i in range(n):
    min_j = i
    for j in range(i, n):
        if A[j] < A[min_j]:
            min_j = j
    if i != min_j:
        A[i], A[min_j] = A[min_j], A[i]
        cnt += 1
print(*A)
print(cnt)


# def selection_sort(collection: list):
#     length = len(collection)
#     for i in range(length-1):
#         least = i
#         for k in range(i+1, length):
#             if collection[k] < collection[least]:
#                 least = k
#         if least != i:
#             collection[least], collection[i] = collection[i], collection[least]
#     return collection
