def card_conv(x: int, r: int) -> str:
    idx = "0123456789abcdefghijklmnopqrstuvwxyz"
    a = []
    result = ""

    while True:
        if r <= x:
            a.append(idx[x%r])
            x = x//r
        else :
            a.append(idx[x])
            break

    # for i in range(len(a)-1,0,-1):
    #     result += str(a[i])

    for i in range(len(a)//2):
        a[i], a[len(a)-i-1] = a[len(a)-i-1], a[i]

    for i in range(len(a)):
        result += str(a[i])
    
    return result


if __name__ == "__main__":
    x = int(input("변환하고 싶은 숫자를 입력하세요 : "))
    r = int(input("변환하고 싶은 진수를 입력하세요(2~36) : "))

    print(f"10진수 {x}를 {r}진수로 변환하면 {card_conv(x,r)}입니다.")
