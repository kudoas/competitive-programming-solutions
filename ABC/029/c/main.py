N = int(input())
abc = 'abc'

# ゴリ押し
for v1 in abc:
    if N == 1:
        print(v1)
    for v2 in abc:
        if N == 2:
            print(v1+v2)
        for v3 in abc:
            if N == 3:
                print(v1+v2+v3)
            for v4 in abc:
                if N == 4:
                    print(v1+v2+v3+v4)
                for v5 in abc:
                    if N == 5:
                        print(v1+v2+v3+v4+v5)
                    for v6 in abc:
                        if N == 6:
                            print(v1+v2+v3+v4+v5+v6)
                        for v7 in abc:
                            if N == 7:
                                print(v1+v2+v3+v4+v5+v6+v7)
                            for v8 in abc:
                                if N == 8:
                                    print(v1+v2+v3+v4+v5+v6+v7+v8)
