# 오른쪽 아래가 직각인 이등변 삼각형

n = int(input('값을 입력하세요 : '))

for i in range(n):
    for j in range(n, i+1, -1):
        print(' ', end= '')
    for k in range(i+1):
        print('^', end = '')
    print()