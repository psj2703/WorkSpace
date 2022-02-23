
# 가로 세로 길이가 정수이고 넓이가 area인 직사각형에서 변의 길이 나열하기


area = int(input("직사각형의 넓이를 입력하세요 : "))
tvalue = 0

for i in range(1, area+1):
    if area % i == 0 :
        tvalue = area / i
    else : continue
    print(f"{i} X {tvalue} = {area}")