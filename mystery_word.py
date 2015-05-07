import random
import sys

def get_text(file_path):

    """This provides the list of words to chose from.

    Functional Argument:
        enter the file path for the list of random words
        this should be `/usr/share/dict/words` """

    words_list =[]
    with open(file_path) as words:
            for word in words:
                words_list.append(word)
    return list_of_words
################################################################################

"""These functions generate the easy, medium, or hard mode.

    Functional Argument:
        include large list of words""" ##change to file path
def easy_words(word_list):              ### include get_text func inside func
    easy_words = []
    for words in word_list:
        if len(words) >= 4 and len(words) <= 6:
            easy_words.append(words)
    return easy_words

def medium_words(word_list):
    medium_words = []
    for words in word_list:
        if len(words)  >= 6 and len(words) <= 8:
            medium_words.append(words)
    return medium_words

def hard_words(word_list):
    hard_words = []
    for words in word_list:
        if len(words) >= 8:
            hard_words.append(words)
    return hard_words

################################################################################



def random_word(word_list):

    """Random Generator
    Functional Argument: (word_list)

    word_list is ***NEED TO CHECK***.""" #I think make file_path

    return random.choice(word_list)

################################################################################

def display_word(word, guess):

    """Display words to user.

    Functional Argument: (word, guess)

    word is the computer generated word
    guess is the list of user guesses. """

    display = ""
    for letter in word:
        if letter in guess:
            display = display + letter.upper() + " "
        else:
            display = display + "_" + " "
    return display[:-1]


################################################################################

def is_word_complete(word, guess):
    """Have the guessed the word completely.

    Functional Argument: (word, guess)

    word is the computer generated word
    guess is the list of user guesses. """

    for letter in word:
        if letter in guess:
            pass
        else:
            return False
    return True

################################################################################

def user_guess():
    """Asks for user to guess a letter.
    Checks for for letter and only one letter"""

    letter_guess = input("Guess a letter\n>")

    if len(letter_guess) != 1:
        print("Please only one letter.")
        return user_guess()

    elif letter_guess.isalpha() == True:
        return letter_guess.upper()

    else:
        print("That is not a letter!")
        return user_guess()

################################################################################

def update_user(count, guess):
    """"Updates users after every guess how many guesses
    they have left and what they have already guessed

    Functional arguments: (count, guess)
    count = the number of guesses so far
    guess = the list of guessed letters"""

    print("You have {} guesses left".format(8 - count))
    print("You have guessed {}".format(guess))

################################################################################
def user_choose_level(a_list):

    """Asking users to choose the level they
    want to play: easy, medium, and hard.

    Functional Argument:

    Must include a list. In the mystery game
    it includes the random_word_list
    which is equal to the get_text(file_path)."""

    level = input("""Please choose which level you would
                  like to play: [E]asy, [M]edium, [H]ard\n> """).upper()

    if level == E:
        return easy_words = easy_words(random_word_list)

    if level == M:
        return medium_words = medium_words(random_word_list)

    if level == H:
        return hard_words = hard_words(random_word_list)

################################################################################

def mystery_game(file_path):
    print("Welcome to the Myster Game! " +
          "It is a lot like hang man except no one gets hurt.")
    count = 8
    guess = []
    random_word_list = get_text(file_path)
    user_choose_level(random_word_list):
###Kep

################################################################################
#if __name__ == "__main__":
