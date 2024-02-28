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

