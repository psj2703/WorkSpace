def sum(n):
    if n == 0:
        return 0
    return n + sum(n-1)

def fibo(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fibo(n - 2) + fibo(n - 1)

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def comb(a, b):

    pass

if __name__ == '__main__':
    print(sum(10)) # 55
    print(sum(100)) # 5050

    print(fibo(1)) # 1
    print(fibo(2)) # 1
    print(fibo(3)) # 2
    print(fibo(4)) # 3
    print(fibo(5)) # 5
    print(fibo(6)) # 8
    print(fibo(7)) # 13
    print(fibo(8)) # 21

    print(factorial(1)) # 1
    print(factorial(2)) # 2
    print(factorial(3)) # 6
    print(factorial(4)) # 24
    print(factorial(5)) # 120

    # print(comb(4,2)) # 6
    # print(comb(5,2)) # 10

