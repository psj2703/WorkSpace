# 1000이하의 소수 나열하기

div_num = 0
counter = 1
x = [2,]

for i in range(3, 1000):
    y = 2
    while i%y:
        div_num += 1
        y += 1
        if y == i:
            x.append(i)
            counter += 1
            break
    
print(x)
print(f"소수의 갯수 : {counter}")
print(f"연산 횟수 : {div_num}")