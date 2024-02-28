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
    logo # Welcome logo with a welcome text (Welcome text used in imported files to align text)
)

# Declaring two global variables as of now. # # # 
emoji_lives = "❤️ "
hangman_graphics = graphics



def print_hangman():
    """
    """
# . . . . 
# . . . . 
# . . . . 


def retrieve_valid_word(wordlist):
    """
    Function that will retrieve a random word from the module(wordlist.py)
    Based on user choice or default quickplay(Easy-mode)
    """
    word = random.choice(wordlist)
    return word.lower()



def hangmanthegame(wordlist):
    """
    Function to play the game, will call other functions accordingly.
    
    Args: 
    - wordlist: list of words for random selection.
    
    Returns:
    - str: random selected word (conv. to lowercase)
    """
    word = retrieve_valid_word(wordlist) # Retrieves the word from wordlist.
    word_letters = set(word) # Converting the word to set of letters. 
    used_letters = set() # Set used letters as empty to store users guessed letters.
    abc = set(string.acsii_lowercase) # Set of all alphabets to lowercase

    print_hangman(0) # Printing the initial hangman drawing at start of the game-round.

    # MAIN GAME LOOP 
    # . . . . 
    # . . . . 
    # . . . . 
    # . . . .  



def gamemenu():
    """
    """
# . . . . 
# . . . . 
# . . . . 
# . . . . 


def play_game():
    """
    Function to initialize the game by calling hangmanthegame().
    """
# . . . . 
# . . . . 
# . . . . 
# . . . . 


def description():
    """
    """
# . . . . 
# . . . . 
# . . . . 
# . . . . 



def difficulty():
    """
    Function to give user choices of various difficulty levels.
    """
# . . . . 
# . . . . 
# . . . . 
# . . . . 


def game_options():
    """
    Function that will display game options to user and require input of choice.
    1. Easy ( 4 Letter word and 5 lives )
    2. Medium ( 6-8 Letter word and 6 lives )
    3. Hard ( 8-11 Letter word and 7 lives )
    """
# . . . . 
# . . . . 
# . . . . 
# . . . . 



def quit_game():
    """
    Function to terminate application.
    """
# . . . . 
# . . . . 
# . . . . 
# . . . . 



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

    if __name__ == "__main__":
        snare_the_rope()



