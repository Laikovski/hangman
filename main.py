import random
import string

def menu():
    choise = input('Type "play" to play the game, "exit" to quit: ')
    if choise == 'play':
        play_game()
    else:
        exit()

def play_game():
    all_words = ['javascript']
    select_word = random.choice(all_words)
    hidden_word = '-' * len(select_word)
    used_letters = []

    print('''H A N G M A N''')
    k = 1
    while k < 10:
        print()
        print(''.join(hidden_word))
        letter = input(f'Input a letter: ')

        if letter in string.ascii_lowercase:
            if letter in used_letters:
                print('You\'ve already guessed this letter')
            elif letter in select_word:
                for i, c in enumerate(select_word):
                    if letter == c:
                        hidden_word = list(hidden_word)
                        hidden_word[i] = c
                        # k += 1
            else:
                print('That letter doesn\'t appear in the word')
                k += 1
            if '-' not in hidden_word:
                print(f'\n{"".join(hidden_word)} \nYou guessed the word!\nYou survived!')
                print()
                menu()
            elif k == 9:
                print('You lost!')
                print()
                menu()
            used_letters.append(letter)
        elif len(letter) > 1:
            print('You should input a single letter')
        elif letter not in string.ascii_uppercase or letter.isupper():
            print('Please enter a lowercase English letter')

menu()
