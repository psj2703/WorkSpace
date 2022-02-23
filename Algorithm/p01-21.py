# 구구단 곱셈표 출력하기

i, k, j = 1, 1, 1

for i in range(2, 10):    
    for j in range(2, 10):
        k = i * j
        if k < 10 :
            print(f'{i} x {j} =  {k}', end='  ')
        else:
            print(f'{i} x {j} = {k}', end='  ')

    print()