def show_hidden_word(secret_word, old_letters_guessed):
    """
                     mamba            m s a s 
    """
    new_word = secret_word
    for old_letter in old_letters_guessed:
        for letter in secret_word:
            if not letter in old_letters_guessed:
                new_word = new_word.replace(letter," _ ")
                       
                     
                  
                   
                
    return new_word

def main():
    old = ["y","u","a","c"]
    print(show_hidden_word("yuval",old))
    
  
    

if __name__ == "__main__":
    main() 