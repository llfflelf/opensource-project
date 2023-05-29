import random
correct_number = ["0", "0", "0", "0"]
correct_number[0] = str(random.randrange(1, 10, 1))
correct_number[1] = correct_number[0]
correct_number[2] = correct_number[0]
correct_number[3] = correct_number[0]

# 숫자가 같을 경우 반복시행
while(correct_number[0] == correct_number[1]):
    correct_number[1] = str(random.randrange(1, 10, 1))
while(correct_number[0] == correct_number[2] or correct_number[1] == correct_number[2]):
    correct_number[2] = str(random.randrange(1, 10, 1))
while(correct_number[0] == correct_number[3] or correct_number[1] == correct_number[3] or correct_number[2] == correct_number[3]):
    correct_number[3] = str(random.randrange(1, 10, 1))

print(correct_number)

try_n = 0
strike = 0
ball = 0

print("숫자야구를 시작합니다.")
print("--------------------------")
while (strike < 4):
    number = str(input("숫자 4자리를 입력하세요: "))

    if len(number) != 4: #숫자 다시 입력
        print("잘못된 입력입니다. 4자리 숫자를 다시 입력해주십시오.")
        continue

    strike = 0
    ball = 0

    for i in range(0, 4): # i 값의 범위 0~3
        for j in range(0, 4):
            if(number[i] == str(correct_number[j]) and i == j):
                strike += 1
            elif(number[i] == str(correct_number[j]) and i != j):
                ball += 1
    print("결과: [",strike,"]스트라이크 [",ball,"]볼")
    try_n += 1

print("--------------------------")
print("축하합니다! 정답입니다!")
print("[",try_n,"]번 만에 맞췄습니다")
print("정답은 [",correct_number,")입니다!")
