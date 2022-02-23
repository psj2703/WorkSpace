# 리스트의 모든 원소를 스캔하기

x = ['john', 'Geroge', 'Paul', 'Ringo']

for i in range(len(x)):
    print(f'x[{i}] = {x[i]}')


# 리스트의 모든 원소를 enumerate()함수로 스캔하기

x = ['john', 'Geroge', 'Paul', 'Ringo']

for i, name in enumerate(x):
    print(f'x[{i}] = {name}')


# 리스트의 모든 원소를 enumerate()함수로 스캔하기(1부터 카운트)

x = ['john', 'Geroge', 'Paul', 'Ringo']

for i, name in enumerate(x, 1):
    print(f'x[{i}] = {name}')


# 리스트의 모든 원소를 스캔(인덱스값 사용x)

x = ['john', 'Geroge', 'Paul', 'Ringo']

for i in x:
    print(f'{i}')