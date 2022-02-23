# 1000이하의 소수 나열하기 
# 개선된 알고리즘

div_num = 0
counter = 2
x = [2,3,]

for i in range(4, 1000):
    for j in range(counter-1):
        div_num += 1
        if i%x[j] == 0:
            break
    else :
        x.append(i)
        counter += 1

print(x)
print(f"소수의 개수 : {counter}")
print(f"연산 횟수 : {div_num}")