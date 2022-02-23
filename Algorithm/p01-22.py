# 왼쪽 아래가 직각인 이등변 삼각형 출력하기


n = int(input("값을 입력하세요 : "))

for i in range(1, n+1):
    for j in range(i):
        print('*', end='')
    print()

