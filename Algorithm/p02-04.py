# 배열 원소의 최대값을 구해서 출력하기(원소값은 난수로 생성)

import random
from max import max_of

print('난수의 최대값을 구합니다')
num = int(input('난수의 갯수를 입력하세요:'))
random_max = int(input('난수의 최대값을 입력하세요:'))
random_min = int(input('난수의 최소값을 입력하세요:'))
x = [None]*num

for i in range(num):
    x[i] = random.randint(random_min, random_max)
  
print(f"{x}")
print(f"생성된 값들 중 최대값은 {max_of(x)}입니다.")