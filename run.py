# Importing Python standard libraries.

from time import sleep
import os
import string
import random

# Importing my module (wordlist.py)

from wordlist import (
    easy_words,  # 1/5 chance on a word with 4 letters
    medium_words,  # 1/5 chance on a word with 5-7 letters
    hard_words,  # 1/5 chance on a word with 8-11 letters
    graphics,  # the hangman drawing index [0-6] 7-drawing stages.
    logo,  # Welcome logo with a welcome text
    endgamevis,  # Game Over ASCII art sign.
    gamedescription,  # Game Description for Option 3.
    RC, GC, YC, RS,  # Colors imported Red, Green, Yellow, Reset
    winnerlogo  # Winner logo!!
)

# Global variables.
EMOJI_LIVES = "❤️ "
HANGMAN_GRAPHICS = graphics
# Declaring variable for system clear to function Unix and Windows
CC = 'clear' if os.name == 'posix' else 'cls'
# Declaring global variable to remove magic number.
MAX_HANGMAN_STAGES = len(HANGMAN_GRAPHICS)


def print_hangman(lives):
    """
    Function to print the hangman graphics in order
    based on the number of lives remaining.

    Added exception handling to catch errors when an invalid nr
    of life would be provided.

    Args:
      * lives (int): Remaining lives in the game.
    """
    try:
        if 0 <= lives < MAX_HANGMAN_STAGES:
            print(HANGMAN_GRAPHICS[lives])
        else:
            raise ValueError("Invalid number of lives! Value out of range")
    except ValueError as e:
        print(f"Error: {e}.\n")


def retrieve_valid_word(wordlist):
    """
    Function that will retrieve a random word from the module (wordlist.py)
    Based on user choice or default quickplay(Easy-mode)

    Arg:
    * wordlist (list): List of words, for random pick.

    Return:
    * str: The randomly selected word converted to lowercase letters.
    """
    secret_word = random.choice(wordlist)
    return secret_word.lower()


def handle_replay():
    """
    Function to handle the option for the user to play again
    after the game is either won or lost.
    By choosing 1 for the main menu and 2 for exit, both need confirmation
    with 'Enter'.
    """
    while True:
        replay = input("Main menu 1, Exit 2, Enter to confirm\n")
        if replay == '1':
            os.system(CC)
            gamemenu()
            game_options()
            break
        elif replay == '2':
            quit_game()
            break
        else:
            print("Invalid option, Either 1 or 2 - confirm with enter!")


def hangmanthegame(wordlist, lives):
    """
    Sets up the Hangman game, where players guess letters
    to unveil the secret word.
    Provides visual feedback with Hangman drawings,
    current word state, and used letters.

    Continues until the player guesses the word or runs out of lives.
    Displays congrats or correct word based on the outcome.

    Includes input validation, checks for repeated letters,
    and handles user interaction.

    Args:
    * wordlist (list): List of words for random pick.
    * lives (int): The number of lives remaining.

    Return:
    * str: The randomly selected word (conv. to lowercase)

    Future Plan:
    * The function is planned to be refactored into smaller functions
    for better readability and maintainability.

    """
    # Retrieves the word from wordlist.
    secret_word = retrieve_valid_word(wordlist)
    # Converting the word to a set of letters.
    word_letters = set(secret_word)
    # Set used letters as empty to store users guessed letters.
    used_letters = set()
    # Set of all alphabets to lowercase
    abc = set(string.ascii_lowercase)

    # Printing the initial hangman drawing at the start of the game-round.
    print_hangman(0)

    # Main game loop
    while word_letters and lives > 0:

        os.system(CC)
        # Display the current state (lives remaining - displayed as hearts)
        print(f"{GC}Lives {EMOJI_LIVES * lives}{RS}")
        # Increment the hangman drawing based on failed attempts.
        print_hangman(MAX_HANGMAN_STAGES - lives)
        print(f"{YC}letters used: {' '.join(used_letters)}{RS}\n")

        word_in_list = [
         letter if letter in used_letters else '_ ' for letter in secret_word
        ]
        """
        Display the current word with a list comprehension we create
        underscores ___ for the user to guess if not letter is in word
        In that case the letter appends to the word.
        """
        print(f"{YC}Secret word: {' '.join(word_in_list)}{RS}\n")

        # Input for the user to guess.
        user_letter = input(f"{YC}Guess the letter: {RS}\n").lower()

        # Validate user input.
        if len(user_letter) != 1 or user_letter not in abc:
            print(f"{RC}Invalid input. Please enter a single letter.{RS}\n")
            sleep(2)
            continue

        # Check user input for already attempted letters.
        if user_letter in used_letters:
            print(f"""{RC}
            Are you looking for the snare?
            You have already used that character.
            Please try again.{RS}
            \n""")
        else:
            used_letters.add(user_letter)

        # Check if user input is in the secret word.
        if user_letter in word_letters:
            word_letters.remove(user_letter)
            print(f"{GC}Correct! {user_letter} is in the secret word{RS}")
            sleep(3)
        else:
            lives -= 1
            print(f"{RC}Incorrect! Are you in a hurry for that snare?{RS}")
            sleep(3)

        if not word_letters:
            os.system(CC)
            print(
                f"{GC}Congratulations!!!{RS}"
                f"You guessed the word: {GC}{secret_word}{RS}"
                )
            print(winnerlogo)
            print(f"You survived the gallow with {lives} ❤️ remaining.")
            sleep(2)
            handle_replay()

    # Game over -> Clear screen -> Display word - Show end game visuals.
    if lives == 0:
        os.system(CC)
        print(endgamevis)  # Visual imported from module.
        print(HANGMAN_GRAPHICS[6])  # Print the last stage of hangman.
        print(f"You ran out of lives. The word was: {GC}{secret_word}{RS}\n")
        handle_replay()


def gamemenu():
    """
    Function to display the logo that includes welcome text,
    Delay added for overall improvement in user experience.
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
    hangmanthegame(selected_level, lives)


def description():
    """
    Function that displays the game description if the user chooses to do so
    as an option from game_options() -> the game description is imported
    from wordlist.py.

    'Enter' as a back to the main menu option added.
    ↓
    Initialize gamemenu() and game_options()
    Delays added for UX/UI.
    """
    print(gamedescription)  # Prints the imported description from wordlist.
    sleep(1)
    # User has a option to press 'Enter' to return to mainmenu.
    if input("Press enter to return to the main menu.\n") == "":
        sleep(1)
        os.system(CC)
        sleep(1)
    # After clear and some delay added the game menu will appear ↓
    gamemenu()
    # and the options with it as on start of the game. ↓
    game_options()


def quit_game():
    """
    Function to terminate the application.
    """
    exit_game = 4
    print("Exiting the game, Hangbye!")
    return exit_game


def difficulty():
    """
    Function to give the user choices of various difficulty levels.
    1. Easy ( 4 Letter word and 5 lives )
    2. Medium ( 6-8 Letter word and 6 lives )
    3. Hard ( 8-11 Letter word and 7 lives )
    """
    while True:
        print("Make your choice carefully, your life may hang on it!\n")
        levels = {
            '1': (easy_words, 5),
            '2': (medium_words, 6),
            '3': (hard_words, 7)
        }
        print(
            f"{YC}1 : Easy\n",
            f"2 : Medium\n",
            f"3 : Hard\n{RS}"
        )
        # User input for difficulty.
        choice = input("Enter your choice by number: \n")

        """
            validate user input
            retrieving difficulty chosen + lives,
            default set to None None as a conditional check.
        """
        selected_level, diff_lives = levels.get(choice, (None, None))
        if selected_level is not None:
            print(
                f"{YC}You have chosen difficulty level: {RS}{GC} {choice}{RS}"
                f"{YC}You will start with lives: {RS}{GC} {diff_lives}{RS} ❤️"
            )
            return selected_level, diff_lives
            # Invalid input msg.
        os.system(CC)
        print("Invalid choice, Please try again. \n")


def game_options():
    """
    Function that will display game options to user:
    1 - Quick play on Easy mode preset default (5 lives)
    2 - Difficulty options: Easy Medium Hard - selection for user.
    3 - Game Description, Short and concise description
    4 - Terminate game
    """
    options = {
        '1': play_game,
        '2': difficulty,
        '3': description,
        '4': quit_game
    }

    while True:
        print(f"""{YC}
        1. Quickplay on Easy mode
        2. Difficulty Options
        3. Game Description
        4. Exit{RS}
        """)
        choice = input("Enter your choice by number:  \n")
        selected_option = options.get(choice)

        # Validate user's choice.
        if selected_option:
            if choice == '1':
                lives = 5
                selected_option(easy_words, lives)
            elif choice == '2':
                selected_level, lives = difficulty()
                play_game(selected_level, lives)
            else:
                selected_option()
            break

        print("Invalid choice. Please try again. \n")


def snare_the_rope():
    """
    ↓↑
    Function that ignites the game, starting with snaring the rope!
    This function is the heart, the engine, Go baby go button.
    The entry point that initializes the app,
    gamemenu()
    game_options()
    """
    gamemenu()
    game_options()


if __name__ == "__main__":
    snare_the_rope()
