
import Hungman.used_functions.print_hungman as stages
import Hungman.used_functions.show_hidden_word as hiddenword
import Hungman.used_functions.valid_input as valid
import Hungman.used_functions.try_update_letter_guessed as sync


def insert_letter(word):
    """
    This function lets the user guess a letter each time,
    Checks if the letter Valid & if the letter in the word.
    The user has maximum of 6 tries.
    :param word: word from the text file
    :type word: str
    """
    used_letter = []
    hidden = ''
    number_of_tries = 1
    while number_of_tries != 7:
        guess_a_letter = input("Guess a letter: ")
        # letter validation
        letter_valid = valid.check_valid_input(guess_a_letter, used_letter)
        if not letter_valid:
            print("X")
        elif guess_a_letter not in word:
            number_of_tries += 1
            print("):")
            stages.print_hangman(number_of_tries)
            print(sync.try_update_letter_guessed(guess_a_letter, used_letter))
        elif guess_a_letter in word:
            sync.try_update_letter_guessed(guess_a_letter, used_letter)
            hidden = hiddenword.show_hidden_word(word, used_letter)
            print(hidden)
        if hidden == word:
            print("Win")
            break
    if number_of_tries == 7:
        stages.print_hangman(number_of_tries)
        print("LOSE")




