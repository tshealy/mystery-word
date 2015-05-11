import random
import os

def get_text(file_path):

    """This provides the list of words to chose from.

    Functional Argument:
        enter the file path for the list of random words
        this should be `/usr/share/dict/words` """

    words_list =[]
    with open(file_path) as words:
            for word in words:
                words_list.append(word[:-1])
    return words_list
################################################################################

"""These functions generate the easy, medium, or hard mode.

    Functional Argument: (a_list)
        Include  list of words"""

def easy_words(a_list):
    easy_words = []
    for word in a_list:
        if len(word) >= 4 and len(word) <= 6:
            easy_words.append(word)
    return easy_words

def medium_words(a_list):
    medium_words = []
    for word in a_list:
        if len(word)  >= 6 and len(word) <= 8:
            medium_words.append(word)
    return medium_words

def hard_words(a_list):
    hard_words = []
    for word in a_list:
        if len(word) >= 8:
            hard_words.append(word)
    return hard_words

################################################################################

def random_word(list):

    """Random Generator
    Functional Argument: (list)

    Must be a list."""

    return random.choice(list)

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

def user_guess(guess):
    """Asks for user to guess a letter.
    Checks for for letter and only one letter"""

    letter_guess = input("Guess a letter\n>").upper()

    if letter_guess == "*":
        return exit()

    if len(letter_guess) != 1:
        print("Please only one letter.")
        return user_guess(guess)

    if letter_guess in guess:
        print("You have already guessed {}. Please guess again.".format(letter_guess))
        return user_guess(guess)

    if letter_guess.isalpha() == True:
        return letter_guess

    else:
        print("That is not a letter!")
        return user_guess(guess)

################################################################################

def update_user(count, guess):
    """"Updates users after every guess how many guesses
    they have left and what they have already guessed

    Functional arguments: (count, guess)
    count = the number of guesses so far
    guess = the list of guessed letters"""

    print("You have {} guesses left".format(count))
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

    if level == "E":
        return easy_words(a_list)

    if level == "M":
        return medium_words(a_list)

    if level == "H":
        return hard_words(a_list)

################################################################################

def random_word_chosen(file_path):

    """This gets the game started and holds the computer's
    chosen word based on level of difficulty.

    Functional Argument: (file_path)
    Must be the file you want to run"""

    print("Welcome to the Myster Game! To quit at anytime enter *.")

    random_word_list = get_text(file_path)
    word_list_for_level_chosen = user_choose_level(random_word_list)
    random_word_chosen = random_word(word_list_for_level_chosen)
    return random_word_chosen

################################################################################

def word_game(file_path):

    """This takes the random word chosen by the computer
    and runs the game until the user wins or loses

    Functional Argument: (file_path)
    Must be the file you want to run"""

    count = 8
    guess_list = []
    random_word = random_word_chosen(file_path).upper()

    while count > 0:
        users_guess = user_guess(guess_list)
        if users_guess not in random_word:
           count = count - 1
        guess_list.append(users_guess)
        sorted_guess_list = sorted(guess_list)
        print(random_word)
        print(display_word(random_word, sorted_guess_list))
        if is_word_complete(random_word, sorted_guess_list) == True:
            os.system('clear')
            print("You Win!\nThe word was {}".format(random_word.title()))
            break
        update_user(count, guess_list)
        if count == 0:
            os.system('clear')
            print("You Lose!\nThe word was {}".format(random_word.title()))
            break
    play_again = input("Would you like to play again? Y/N\n> ").upper()
    if play_again == "Y":
        return word_game(file_path)
    else:
        return exit()

################################################################################

# def counting(count, random_word, users_guess):
#
#     """If the user chooses correctly the number of guesses does not subtract."""
#
#     if users_guess not in random_word:
#         count = count - 1

################################################################################

if __name__ == "__main__":
    word_game("/usr/share/dict/words")
