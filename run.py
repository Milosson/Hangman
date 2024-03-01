# Importing Python standard libraries.

from time import sleep # Sleep function from time module for adding delays between transitions.
import os # Os module as clear function for wiping screen
import string # String module to use ascii.lower for input validation
import random # Random module to retrive a random word in the right difficulty cat.

# Importing my module (wordlist.py)

from wordlist import (
    easy_words, # 1/5 chance on a word with 4 letters
    medium_words, # 1/5 chance on a word with 5-7 letters
    hard_words, # 1/5 chance on a word with 8-11 letters
    graphics, # the hangman drawing
    logo, # Welcome logo with a welcome text (Welcome text used in imported files to align text)
    endgamevis # Game Over ascii art sign.
)

# Declaring two global variables as of now. # # # 
EMOJI_LIVES = "❤️ "
HANGMAN_GRAPHICS = graphics
# Declaring variable for system clear to function Unix and Windows 
CC = 'clear' if os.name == 'posix' else 'cls'



def print_hangman(lives):
    """
    Function to print the hangman graphics in order
    based on number of lives remaining.

    Args: 
     * lives (int): Remaining lives in game.
    """
    if 0 <= lives < len(HANGMAN_GRAPHICS): 
        print(HANGMAN_GRAPHICS[lives])
        else:
            print("Invalid number of lives provided.\n")




def retrieve_valid_word(wordlist):
    """
    Function that will retrieve a random word from the module(wordlist.py)
    Based on user choice or default quickplay(Easy-mode)

    Arg: 
    * wordlist (list): List of words, for random pick.

    Return:
    * str: The randomly selected word converted to lowercase letters.
    """
    secret_word = random.choice(wordlist)
    return word.lower()



def hangmanthegame(wordlist, lives):
    """
    Function to play the game, will call other functions accordingly.
    
    Args: 
    * wordlist (list): List of words for random pick.
    * lives (int): The number of lives remaining.
    
    Return:
    * str: The random selected word (conv. to lowercase)
    """
    secret_word = retrieve_valid_word(wordlist) # Retrieves the word from wordlist.
    word_letters = set(secret_word) # Converting the word to set of letters. 
    used_letters = set() # Set used letters as empty to store users guessed letters.
    abc = set(string.acsii_lowercase) # Set of all alphabets to lowercase

    print_hangman(0) # Printing the initial hangman drawing at start of the game-round.

    # Main game loop
    while word_letters and lives > 0:
        os.system(CC)
        # Display the current state (lives remaining - displayed as hearts)
        print(f"Lives {EMOJI_LIVES * lives}")
        # Print the initial hangman drawing at start of game round.
        print_hangman(0)
        print(f"letter used: {' '.join(used_letters)}\n")

      
        word_in_list = [
            letter if letter in used_letters else '_ ' for letter in secret_word
        ]   """
         Display the current word with a list comprehension we create
         underscores ___ for the user to guess if not letter is in word
         In that case the letter appends to the word. 
        """
        print(f"Secret word: {' '.join(word_in_list)}\n")

        # Input for user to guess.
        user_letter = input("Guess the letter: \n").lower()

        # Validate user input.
        if len(user_letter) != 1 or user_letter not in abc:
            print("Invalid input. Please enter a single letter.\n")
            continue

        # Check user input for already attempted letters.
        if user_letter in used_letters:
            print("""
            Are you looking for the snare?
            You have already used that character.
            Please try again. 
            \n""")
            else:
                used_letters.add(user_letter)

            # Check if user input is in the secret word.
            if not word_letters:
                os.system(CC)
                print(
                f"CONGRATUUUUULATIONAAAAZ!!!\n"
                f"You are the winner! you had {lives} lives left.\n"
                f"You guessed the word: {secret_word}\n"
                )
                break
    # Game over -> Clear screen ->
    if lives == 0:
        os.system(CC)
        print(endgamevis) # Visual imported from module.
        print(HANGMAN_GRAPHICS[6]) # Print last stage of hang man.
        print(f"You ran out of lives. The word was: {word}\n")




def gamemenu():
    """
    Function to display the logo that includes welcome text,
    Delay added for over all improvment in user experience.
    """
    print(logo)
    sleep(1)


def play_game(selected_level, lives):
    """
    Function will be called by game_options() -> snare_the_rope().

    Args: 
    * selected_level (int): Users selected difficulty level
    * lives (int): The number of lives that matches with the users lvl choice.
    """
    print("Get ready...\n")
    sleep(1)
    print("Hang in there, hangman crew fitting the snare just for YOU!\n")
    sleep(2)
    print("buuuh! Something something very scary...")
    sleep(2)



def description():
    """
    Function that display the game description if user choose to do so 
    as an option from game_options() -> the game description is imported 
    from wordlist.py.
    
    'Enter' as a back to main menu option added. 
    ↓ 
    Initialize gamemenu() and game_options()

    Delays added for UX/UI.    
    """
    print(gamedescription) # Prints the imported description from wordlist.
    sleep(1)
    if input("Press enter to return to the main menu.\n") == "": # User has option to 'Enter' to return
    sleep(1)
    os.system(CC)
    sleep(1)
    gamemenu() # After clear and some delay added the game menu will appear ↓
    game_options() # and the options with it as on start of the game.




def difficulty():
    """
    Function to give user choices of various difficulty levels.
    1. Easy ( 4 Letter word and 5 lives )
    2. Medium ( 6-8 Letter word and 6 lives )
    3. Hard ( 8-11 Letter word and 7 lives )
    """
    




def game_options():
    """
    Function that will display game options to user and require input of choice.
    """
    options = {
        '1' : play_game,
        '2' : difficulty,
        '3' : description,
        '4' : quit_game 
    }

    choice = input("Enter your choice by number:  \n")
    selected_option = options.get(choice)

    # Validate user's choice.
    if selected_option:
        if choice == '1':
            lives = 5
            selected_option(easy_words, lives)
            elif choice == '2':
                selected_level, lives = difficulty()
                play_game(selected, lives)
                else: 
                    selected_option()
                    break

        print("Invalid choice. Please try again. \n")






def quit_game():
    """
    Function to terminate application.
    """
    exit_game = 4
    print("Exiting the game, Hangbye!")
    return 4



def snare_the_rope():
    """
    ↓↑
    Function that ignites the game, starting with snaring the rope!
    This function is the heart, the engine, Go baby go button.
    The entry point that initializes the app, 
    gamemenu()
    game_options()
    """
     # gamemenu()
     # game_options()
     pass


    if __name__ == "__main__":
        snare_the_rope()





