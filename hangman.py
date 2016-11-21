#!/usr/bin/env python3
# This first line is for Unix systems, it tells the system what program to run.
# Here it calls python3 in whichever environment is being used.

""" (this is a long comment)
This example python script creates runs a simple hangman game.
The user must guess letters until they guess the entire word or they reach the
maximum number of guesses (which is set to six).
"""

# imports of libraries
import sys
import os
import random

# constants
DEFAULT_WORDS = [
    "ransom", "cheetah", "tangent", "turkey", "zebra", "astronaut", "volcano",
    "machine", "ghost", "cosmonaut", "bizarre", "mutation", "asteroid", "paranoia",
    "creativity", "pneumatic", "gradient", "terminator"
]

HANGMAN = """
      +----
          |
          |
          |
        ^^^^^
"""

NUMBER_OF_GUESSES = 6

def draw_hangman(number):
    """This is the method that draws the hangman given the number of guesses."""
    current_hangman = HANGMAN

    # notice that Python is space sensitive instead of using brackets
    if number >= 1:
        current_hangman[19] = '0'
    if number >= 2:
        current_hangman[18] = '\\'
    if number >= 3:
        current_hangman[20] = '/'
    if number >= 4:
        current_hangman[31] = '|'
    if number >= 5:
        current_hangman[42] = '/'
    if number >= 6:
        current_hangman[18] = ' '
        current_hangman[20] = ' '
        current_hangman[30] = '/'
        current_hangman[32] = '\\'
        current_hangman[44] = '\\'

    print(current_hangman)


def show_guess(guess, letter, misses,):
    """This function prints the guess at each iteration."""
    n = len(word)
    print_string = """
    Word:
    Letter:
    Misses:

    """

    pass


def update_guess(word, guess, letter):
    """This method updates the guess."""
    pass


def generate_word():
    """Generate the word to be guessed."""
    n_rand = random.randint(0,len(DEFAULT_WORDS)-1)
    return DEFAULT_WORDS[n_rand]

# the "main" function
def main():
    # my code here
    the_word = generate_word()
    # print hangman


# This is standard python convention that allows
if __name__ == "__main__":
    main()
