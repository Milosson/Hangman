easy_words = ["hello", "apple", "smile", "happy", "blue"]

medium_words = ["guitar", "breeze", "puzzle", "laughter", "sunshine"]

hard_words = ["serendipity", "ebullient", "ubiquity", "effectiveness", "translingual"]

graphics = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========''']


logo = f""" {RC}

__ __  ____ ____   ____      ___ ___  ____ ____  
|  |  |/    |    \\ /    |    |   |   |/    |    \\   
|  |  |  o  |  _  |   __|    | _   _ |  o  |  _  |
|  _  |     |  |  |  |  |    |  \\_/  |     |  |  |
|  |  |  _  |  |  |  |_ |    |   |   |  _  |  |  |
|  |  |  |  |  |  |     |    |   |   |  |  |  |  |
|__|__|__|__|__|__|___,_|    |___|___|__|__|__|__|
           {RS}
            {YC} 
                Welcom to Hangman!
                
          The perfect place to learn to spell,
          or just to hang man - your choice! {RS}
                                  
"""

gamedescription = f"""
Hangman is a word-guessing game where players try to guess a hidden word one letter at a time.
Incorrect guesses result in the drawing of a hangman figure and lose a life.
Player is in a position of 5 lives at easy mode, 6 for medium, and 7 for hard mode activated.

Quick play by choosing option 1 (Default level: {GC}Easy{RS})

Choose Difficulty by option 2 in the game menu:

  Option 1: {GC}Easy{RS} ( 4 Letter word + 5 lives ❤️ ) 

  Option 2: {YC}Medium{RS} ( 6-8 Letter word + 6 lives ❤️ )

  Option 3: {RC}Hard{RS} ( 8-11 Letter word + 7 lives ❤️ )
"""



endgamevis = f"""{RC}


      ██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗ 
      ██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗
      ██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝
      ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗
      ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║
      ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝
                                                                          

{RS}"""