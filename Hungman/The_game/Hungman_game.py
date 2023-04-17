import Hungman.file_path_function as file_path
import Hungman.used_functions.choose_word as choose_word
import Hungman.used_functions.print_hungman as stages
import Hungman.used_functions.insert_letter as insert
import Hungman.used_functions.first_time_hidden_word as hid
import Hungman.used_functions.first_page as first_page


def main():
    first_page.first_page()   # first page
    path = file_path.get_path("Words.txt")  # path to the file
    index = input("Enter index: ")  # given by the user
    print("\n")
    word = choose_word.choose_word(path, int(index))   # The special word
    print("Lets Start! Have fun :) \n")
    stages.print_hangman(1)      # The first stage
    hid.hidden_start_word(word)      # Print the hidden word
    insert.insert_letter(word)      # User input - The Main Game -
    print("The word was : " + word)      # The actual word at the End


if __name__ == "__main__":
    main()

