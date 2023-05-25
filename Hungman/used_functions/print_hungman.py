
def print_hangman(num_of_tries):
    """ This function prints the Hangman stages.
        Everytime the user fails to get the word right
        it prints the matching stage.
        :param num_of_tries: The current number of fails the user has.
        :type num_of_tries: int
    """
    for x in range(num_of_tries + 1):
        if x == num_of_tries:
            print(HANGMAN_PHOTOS[x])


HANGMAN_PHOTOS = {1: "x-------x   ",
                  2: """x-------x
|
|       
|
|
| """,
                  3: """x-------x
|       |
|       0
|      
|
| """,
                  4: """x-------x
|       |
|       0
|       | 
|
| """,
                  5:"""x-------x
|       |
|       0
|      /|\ 
|
| """,
                  6:"""x-------x
|       |
|       0
|      /|\ 
|      / 
|""",
                  7:"""x-------x
|       |
|       0
|      /|\ 
|      / \  """}



