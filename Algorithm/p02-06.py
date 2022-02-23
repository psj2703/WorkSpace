# 뮤터블 시퀀스 원소를 역순으로 정렬

from typing import Any, MutableSequence

def reverse_array(a: MutableSequence) -> Any:
    for i in range((len(a))//2):
        a[i], a[len(a)-i-1] = a[len(a)-i-1], a[i]
    return a

if __name__ == '__main__':
    print('배열 원소를 역순으로 정렬합니다.')
    nx = int(input('원소 수를 입력하세요 : '))
    x = [None]*nx

    for i in range(nx):
        x[i] = int(input(f'x[{i}]값을 입력하세요'))

    reverse_array(x)

    print('배열 원소를 역순으로 정렬했습니다.')
    for i in range(nx):
        print(f'x[{i}] = {x[i]}')


