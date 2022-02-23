# 10진수 정수값을 입력받아 2~36 진수로 변환하기

def card_conv(x: int, r: int) -> str:
    '''정수값 x를 r진수로 변환한 뒤 그 수를 나타내는 문자열을 반환'''
    
    # num = 1
    # x1 = x
    # while r < x1:
    #     x1=x1//r
    #     num += 1

    conv_list = []
    
    while True:
        conv_list.append(x%r)
        x = x//r
        if x < r:
            conv_list.append(x)
            break
 
    conv_str = ""
    for i in range(len(conv_list)):
        conv_str+=str(conv_list[len(conv_list)-i-1])

    return conv_str


if __name__ == "__main__":
    x = int(input("변환하고 싶은 숫자를 입력하세요 : "))
    r = int(input("변환하고 싶은 숫자를 입력하세요(2~36) : "))

    print(f"10진수 {x}를 {r}진수로 변환하면 {card_conv(x,r)}입니다.")

    # print(f"10진수 {x}는 {r}진수로 변환하면 {card_conv(x,r)}입니다.")