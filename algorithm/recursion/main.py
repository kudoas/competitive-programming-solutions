# 再帰関数：終了条件を必ずつける事！
def fact(n):
    if n == 0:
        return 1
    return n*fact(n-1)


print(fact(4))


# フィボナッチ数列
def fib(n):
    if n <= 1:
        return n
    return fib(n-1)+fib(n-2)


print(fib(21))


# memo
