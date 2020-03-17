S = input()+'?'
ls = []
cnt = 1

for i in range(len(S)-1):
    if S[i] == S[i+1]:
        cnt += 1
    else:
        ls.append(S[i]+str(cnt))
        cnt = 1

print(''.join(ls))
