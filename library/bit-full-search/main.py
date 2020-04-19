# bit全探索
money = 300
item = (("みかん", 100), ("りんご", 200), ("ぶどう", 300))
n = len(item)

# 全て網羅できる桁数の2進数を用意
for i in range(2**n):
    bag = []
    # ここが大事：用意したbitを１つずつ桁数分回してチェック
    for j in range(n):
        # i >> j：bitシフト
        if (i >> j & 1):
            bag.append(item[j][0])
    print(bin(i), bag)
