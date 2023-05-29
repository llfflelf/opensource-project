import random
from hangman_visual import lives_visual_dict
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    while True:
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

        play_again = input("게임을 다시 시작하시겠습니까? (Y/N): ")
        if play_again.upper() != "Y":
                break


def generate_correct_number(digit_count):
    correct_number = []
    for _ in range(digit_count):
        digit = str(random.randint(1, 9))
        while digit in correct_number:
            digit = str(random.randint(1, 9))
        correct_number.append(digit)
    return correct_number


def ballsAndCows():
    while True:
        difficulty = input("게임 난이도를 선택하세요 (1: 쉬움, 2: 보통, 3: 어려움): ")

        if difficulty == '1':
            digit_count = 3
            max_attempts = 10
        elif difficulty == '2':
            digit_count = 4
            max_attempts = 7
        elif difficulty == '3':
            digit_count = 4
            max_attempts = 5
        else:
            print("유효하지 않은 선택입니다. 보통 난이도로 게임을 시작합니다.")
            digit_count = 4
            max_attempts = 7

        correct_number = generate_correct_number(digit_count)
        print(correct_number)
        print("숫자야구를 시작합니다.")
        print("--------------------------")

        try_n = 0
        strike = 0
        ball = 0

        while (strike < digit_count) and (try_n < max_attempts):
            number = input("숫자 {}자리를 입력하세요: ".format(digit_count))

            if len(number) != digit_count or not number.isdigit():
                print("잘못된 입력입니다. {}자리 숫자를 다시 입력해주십시오.".format(digit_count))
                continue

            strike = 0
            ball = 0

            for i in range(digit_count):
                for j in range(digit_count):
                    if (number[i] == correct_number[j] and i == j):
                        strike += 1
                    elif (number[i] == correct_number[j] and i != j):
                        ball += 1
            print("결과: [", strike, "]스트라이크 [", ball, "]볼")
            try_n += 1
            remain_number = max_attempts - try_n
            print("남은 시도 횟수:", remain_number)

        print("--------------------------")
        if strike == digit_count:
            print("축하합니다! 정답입니다!")
            print("[", try_n, "]번 만에 맞췄습니다")
        else:
            print("아쉽습니다. 정답은 [", ''.join(correct_number), "]입니다!")

        play_again = input("게임을 다시 시작하시겠습니까? (Y/N): ")
        if play_again.upper() != "Y":
            break

def main():
    while True:
        print("안녕하세요. 게임을 선택해주세요.")
        print("1. 행맨")
        print("2. 숫자야구")
        print("3. 종료")
        choice = input("선택: ")

        if choice == "1":
            hangman()
        elif choice == "2":
            ballsAndCows()
        elif choice == "3":
            print("게임을 종료합니다.")
            break
        else:
            print("잘못된 선택입니다.")


if __name__ == '__main__':
    main()
