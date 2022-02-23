from typing import Any, Sequence

def max_of(a: Sequence) -> Any:
    max_num = a[0]
    for i in a:
        if i >= max_num:
            max_num = i
    return max_num

if __name__ == '__main__':
    print("배열의 최값을 구합니다")
    num = int(input("원소 수를 입력하세요 : "))
    x = [None]*num

    for i in range(num):
        x[i] = int(input(f'x[{i}]값을 입력하세요 : '))

    print(f'최대값은 {max_of(x)}입니다')