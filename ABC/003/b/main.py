S = input()
T = input()

free = set('atcoder')
cnt = 0

for s, t in zip(S, T):
    if s == t != '@':
        cnt += 1
    if s == t == '@':
        cnt += 1
    if s == '@' and t in free:
        cnt += 1
    if s in free and t == '@':
        cnt += 1

answer = 'You can win' if cnt == len(S) else 'You will lose'
print(answer)
