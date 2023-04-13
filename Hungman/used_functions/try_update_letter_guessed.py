def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """ 
    this function adds NEW letter to the list 
    and shows error if the letter already exist.
    :param: letter guessed by the user 
    :param: list of old guessed letters
    :type params: str
    :return: True if valid, False if invalid
    """
    letter_guessed = letter_guessed.lower()
    if len(letter_guessed) > 1:
        return False
    elif not letter_guessed.isalpha():
        return False
    elif old_letters_guessed.count(letter_guessed) >= 1:
        return False
    elif letter_guessed.isalpha() and len(letter_guessed) == 1 and old_letters_guessed.count(letter_guessed) == 0:
        old_letters_guessed += [letter_guessed]
        old_letters_guessed.sort()
        letters = (" -> ".join(old_letters_guessed).lower())
        return letters
    else:
        print("Error")



def main():
    old_letters = ["r","a","p","w"]
    x = try_update_letter_guessed("w",old_letters)
    if x is False:
        old_letters.sort()
        print("X")
        print(" -> ".join(old_letters).lower())


if __name__ == "__main__":
    main()
    