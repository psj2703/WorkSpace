from card_conv import card_conv

if __name__ == "__main__":
    print('10진수를 n진수로 변환합니다.')

    while True:
        x = int(input("다른 진수로 변환시킬 10진수의 값을 입력하세요 : "))
        if x > 0:
            break

    while True:
        y = int(input("몇 진수로 변환하시겠습니까?(2~36) : "))
        if 2 <= y <= 36 :
            break

    print(f"10진수 {x}를 {y}진수로 변환 시키면 {card_conv(x,y)}이 됩니다.")