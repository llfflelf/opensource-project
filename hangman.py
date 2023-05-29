import random
from words import words
from hangman_visual import lives_visual_dict
import string


def get_valid_word(words):
    word = random.choice(words)  # randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed

    lives = 7

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
            print('\nYou have already used that letter. Guess another letter.')

        else:
            print('\nThat is not a valid letter.')

    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print(lives_visual_dict[lives])
        print('당신은 죽었습니다. 맞춰야 할 단어는', word)
    else:
        print('야호! 당신은 단어를 맞췄습니다. 단어는', word, '!!')


if __name__ == '__main__':
    hangman()