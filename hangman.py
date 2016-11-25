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
# import readline

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

NUMBER_OF_MISSES = 6

def draw_hangman(number):
    """This is the method that draws the hangman given the number of guesses."""
    current_hangman = list(HANGMAN)

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

    print("".join(current_hangman))


def get_new_letter():
    """This function asks the user to enter a letter."""
    letter = input("Enter your guess: ")
    if not len(letter) == 1:
        print("Only one letter guesses accepted. Try again!")
        return get_new_letter()
    elif not letter.isalpha():
        print("This is not a letter. Try again!")
        return get_new_letter()
    return letter


def show_guess(guess_word, guesses, misses):
    """This function prints the guess at each iteration."""
    # word_string = ""
    # for i in range(0,n):
    guesses_string = ""
    if guesses:
        guesses_string = "".join([c+(", ") for c in guesses])

    print_string = """
    Word:    {}
    Misses:  {}
    Guesses:  {}

    """.format("".join([c+(" ") for c in guess_word]),
               misses,
               guesses_string)

    print(print_string)


def update_guess(word, guess, letter):
    """This method updates the guess."""
    new_guess = list(guess)
    # there are more efficient ways of doing this but I wanted to demonstrate a for loop in python
    miss = True
    for i,c in enumerate(word):
        if c.lower() == letter.lower():
            miss = False
            new_guess[i] = letter.lower()
    # here we return 2 values, the guess and true/false (boolean) if there was a miss
    return ("".join(new_guess), miss)


def generate_word():
    """Generate the word to be guessed."""
    # TODO
    # add other methods to get words:
    #   * NLTK database
    #   * pull from some online source with wotd?
    if False:
        n_rand = random.randint(0,len(DEFAULT_WORDS)-1)
        return (DEFAULT_WORDS[n_rand], NULL)

    if True:
        import requests
        from lxml import html
        # get a random word from randomword.com
        randomword_page = requests.get('https://randomword.com/')
        tree = html.fromstring(randomword_page.content)
        # use xpath to get the word we want on the page
        return (tree.xpath('//div[@id="random_word"]/text()')[0],
                tree.xpath('//div[@id="random_word_definition"]/text()')[0])

def print_congratulations(word, definition, misses):
    """Print congratulations, you won!"""
    print("\n    The word is \'{}\'.".format(word))
    print("    Its definition is \'{}\'.".format(definition))
    print("\n    Congratulations you won with {} misses!\n\n".format(misses))

def print_condolences(word, definition):
    """Print condolescenes."""
    print("\n    The word is \'{}\'".format(word))
    print("    Its definition is \'{}\'.".format(definition))
    print("\n    Sorry you lost and someone died! You need more education.\n")

def play_again():
    """Start again?"""
    answer = input("Would you like to play again [y|n]?")
    if answer[0].lower() == 'y':
        main()
    elif answer[0].lower() == 'n':
        exit()
    else:
        print("I did not recognize your answer.")
        play_again()


# the "main" function
def main():
    # my code here
    misses = 0
    guesses = []
    (the_word, definition) = generate_word()
    guess_word = "_"*len(the_word)
    letter = ""
    check = False
    # print hangman
    print("\n\n    LET'S PLAY A GAME!")
    while misses < NUMBER_OF_MISSES:
        draw_hangman(misses)
        show_guess(guess_word, guesses, misses)
        # update letter
        guesses.insert(0,get_new_letter())
        # update the guess word
        (guess_word, miss) = update_guess(the_word, guess_word, guesses[0])
        # check if they won and exit
        if not '_' in guess_word:
            print_congratulations(guess_word, definition, misses)
            return
        # if they missed increment misses
        if miss:
            misses += 1

    draw_hangman(misses)
    print_condolences(the_word, definition)
    return


# This is standard python convention that allows
if __name__ == "__main__":
    main()
    while True:
        play_again()
