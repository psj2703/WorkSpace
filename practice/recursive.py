def sum(n):
    result = 0
    for i in range(1, n + 1):
        result += i
    return result


def sum2(n):
    if n == 1:
        return 1

    return sum2(n-1) + n



def fibo(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
   
    return fibo(n-1) + fibo(n-2)


def C(a, b):
    print(f"C({a}, {b}) >>>")
    if a == b:
        return 1
    if b == 0:
        return 1
    
    if b > a/2:
        return C(a, a-b)

    return C(a-1, b-1) + C(a-1, b)


if __name__ == '__main__':
    print(sum2(5)) # 55
    # print(sum(100)) # 5050
”
    # print(fibo(1)) # 1
    # print(fibo(2)) # 1
    # print(fibo(3)) # 2
    # print(fibo(4)) # 3
    # print(fibo(5)) # 5
    # print(fibo(6)) # 8
    # print(fibo(7)) # 13
    # print(fibo(8)) # 21
   
    # print(C(5,3))
    