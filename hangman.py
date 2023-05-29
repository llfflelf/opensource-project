import random
from hangman_visual import lives_visual_dict
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():

    difficulty = input("게임 난이도를 선택하세요 (1: 쉬움, 2: 보통, 3: 어려움): ")

    if difficulty == '1':
        from words_easy import words
        lives = 10
    elif difficulty == '2':
        from words_medium import words
        lives = 7
    elif difficulty == '3':
        from words_hard import words
        lives = 5
    else:
        print("유효하지 않은 선택입니다. 보통 난이도로 게임을 시작합니다.")
        from words_medium import words
        lives = 7
    
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed

    print('정답',word)

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        print('당신은 ', lives, '목숨이 남았고 당신이 선택한 알파벳: ', ' '.join(used_letters))

        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict[lives])
        print('현재 단어: ', ' '.join(word_list))

        user_letter = input('단어 선택: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives = lives - 1  # takes away a life if wrong
                print('\n당신이 선택한 알파벳', user_letter, '은(는) 단어안에 존재하지 않습니다.')

        elif user_letter in used_letters:
            print('\n이전에 이미 선택한 글자입니다. 다른 글자를 선택해주세요.')

        else:
            print('\n유효하지 않은 글자입니다.')


    if lives == 0:
        print(lives_visual_dict[lives])
        print('당신은 죽었습니다. 맞춰야 할 단어는', word)
    else:
        print('야호! 당신은 단어를 맞췄습니다. 단어는', word, '!!')


def ballsAndCows():
    correct_number = ["0", "0", "0", "0"]
    correct_number[0] = str(random.randrange(1, 10, 1))
    correct_number[1] = correct_number[0]
    correct_number[2] = correct_number[0]
    correct_number[3] = correct_number[0]

    # 숫자가 같을 경우 반복시행
    while (correct_number[0] == correct_number[1]):
        correct_number[1] = str(random.randrange(1, 10, 1))
    while (correct_number[0] == correct_number[2] or correct_number[1] == correct_number[2]):
        correct_number[2] = str(random.randrange(1, 10, 1))
    while (correct_number[0] == correct_number[3] or correct_number[1] == correct_number[3] or correct_number[2] ==
           correct_number[3]):
        correct_number[3] = str(random.randrange(1, 10, 1))

    print(correct_number)

    try_n = 0
    strike = 0
    ball = 0

    print("숫자야구를 시작합니다.")
    print("--------------------------")
    while (strike < 4):
        number = str(input("숫자 4자리를 입력하세요: "))

        if len(number) != 4:  # 숫자 다시 입력
            print("잘못된 입력입니다. 4자리 숫자를 다시 입력해주십시오.")
            continue

        strike = 0
        ball = 0

        for i in range(0, 4):
            for j in range(0, 4):
                if (number[i] == str(correct_number[j]) and i == j):
                    strike += 1
                elif (number[i] == str(correct_number[j]) and i != j):
                    ball += 1
        print("결과: [", strike, "]스트라이크 [", ball, "]볼")
        try_n += 1

    print("--------------------------")
    print("축하합니다! 정답입니다!")
    print("[", try_n, "]번 만에 맞췄습니다")
    print("정답은 [", correct_number, ")입니다!")

def main():
    print("안녕하세요! 플레이하실 게임을 선택해주세요!")
    print("1. 행맨")
    print("2. 숫자야구")
    choice = input("선택: ")

    if choice == "1":
        hangman()
    elif choice == "2":
        ballsAndCows()
    else:
        print("잘못된 선택입니다.")


if __name__ == '__main__':
    main()
