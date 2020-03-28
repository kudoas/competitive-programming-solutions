n = int(input())
aa = list(map(int, input().split()))

rate = [False] * 9

# Trueと1の混在に注意
for a in aa:
    if a < 400:
        rate[0] = 'T'
    elif a < 800:
        rate[1] = 'T'
    elif a < 1200:
        rate[2] = 'T'
    elif a < 1600:
        rate[3] = 'T'
    elif a < 2000:
        rate[4] = 'T'
    elif a < 2400:
        rate[5] = 'T'
    elif a < 2800:
        rate[6] = 'T'
    elif a < 3200:
        rate[7] = 'T'
    else:
        rate[8] += 1

not_free_rate = rate.count('T')
free_rate = rate[8]


if not_free_rate == 0:
    min_num = 1
else:
    min_num = not_free_rate


print(min_num, not_free_rate+free_rate)
