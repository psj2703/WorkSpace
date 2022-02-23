from max import max_of

print('배열의 최대값을 구합니다.')
print('주의 : "end"를 입력하면 종료됩니다.')

number = 0
counting = 0
x = []

while True:
    number = input("정수값을 입력하세요 : ")
    if number == "end":
        break
    number=int(number)
    x.append(number)
    counting += 1

print(f"입력하신 수는 {counting}개입니다.")
print(f"입력한 수 가운데 최대값은 {max_of(x)}입니다.")