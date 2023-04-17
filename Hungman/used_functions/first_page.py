def first_page():
    """
    This function prints the first page of the game
    and the maximum number of tries the user has
    """
    hangman_welcome_screen =("""welcome to hungman
     _    _                                         
    | |  | |                                        
    | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
    |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
    | |  | | (_| | | | | (_| | | | | | | (_| | | | |
    |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |                      
                        |___/
    """)

    max_tries = "6"

    print(hangman_welcome_screen)
    print("You have maximum of : " + max_tries + " tries \n" )

