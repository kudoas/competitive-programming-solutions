import itertools
import sys


def main():
    input = sys.stdin.readline
    n = int(input())
    L = map(int, input().split())
    cnt = 0

    ls = itertools.combinations(L, 3)

    for l in ls:
        if sum(l) > max(l)*2:
            cnt += 1

    print(cnt)


if __name__ == '__main__':
    main()
