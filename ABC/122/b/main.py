S = input()
L = len(S)
answer = 0

# 文字列の全パターンを検索
for left in range(L):
    for right in range(left, L):
        T = S[left:right+1]
        # ACGT以外の文字が入っていた時点で連続した文字列は切れている
        if set(T) <= set('ACGT'):
            answer = max(answer, right-left+1)

print(answer)

# 露骨に原始的な方法
# m = 0
# cnt = 0

# for s in S:
#     if s in 'A':
#         cnt += 1
#     elif s in 'C':
#         cnt += 1
#     elif s in 'G':
#         cnt += 1
#     elif s in 'T':
#         cnt += 1
#     else:
#         cnt = 0
#     m = max(m, cnt)
# print(m)
