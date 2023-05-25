def check_valid_input(letter_guessed, old_letters_guessed):
    """ 
    this function checks the input of the user 
    and validate.
    :param: letter guessed by the user
    :type params: str
    :return: True if valid, False if invalid
    """
    if len(letter_guessed) > 1 :
        return False
    elif not letter_guessed.isalpha():
        return False
    elif old_letters_guessed.count(letter_guessed) >= 1:
        return False
    elif letter_guessed.isalpha() and len(letter_guessed) == 1 and old_letters_guessed.count(letter_guessed) == 0:
        return True
    

def main():
    past_letters = ["a","v","s"]
    print(check_valid_input("s", past_letters))


if __name__ == "__main__":
    main()
