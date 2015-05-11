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

def longest_word(file_path):
    list = get_text(file_path)
    list_of_lengths = []
    for word in list:
        list_of_lengths.append(len(word))
    return max(list_of_lengths)

################################################################################

def words_grouped_by_length(file_path):
    list = get_text(file_path)
    length_dict = {}
    word_groups = range(4, longest_word(file_path) + 1) #equals 24 + 1
    for index in word_groups:
        for word in list:
            if len(word) == index:
                length_dict.setdefault(index, []).append(word)
    return length_dict

################################################################################

def level_mode(file_path):

    """Asking users to choose the level they
    want to play: easy, medium, and hard.

    Functional Argument:

    Must include a list. In the mystery game
    it includes the random_word_list
    which is equal to the get_text(file_path)."""

    level = input("""Please choose which level you would
                  like to play: [E]asy, [M]edium, [H]ard\n> """).upper()

    if level == "E":
            return [4,5,6]

    if level == "M":
            return [6,7,8]

    if level == "H":
            return [range(8,25)]

################################################################################

def user_guess():
    """Asks for user to guess a letter.
    Checks for letter, and only one letter"""

    letter_guess = input("Guess a letter\n>").upper()

    if letter_guess == "*":
        return exit()

    if len(letter_guess) != 1:
        print("Please only one letter.")
        return user_guess()

    # if letter_guess in guess:
    #     print("You have already guessed {}. Please guess again.".format(letter_guess))
    #     return user_guess()

    if letter_guess.isalpha() == True:
        return letter_guess

    else:
        print("That is not a letter!")
        return user_guess()

################################################################################

def demon_list():
    """This sorts all the lists and then sends the list
    with the most words to the display function.

    Functional Argument:
    user_letter = the letter chosen by the player.
    list = the randomly generated list based on the level of play."""



    users_guess = user_guess()
    word_groups = words_grouped_by_length(file_path)
    length_groups = level_mode(file_path)
    demon_dict = {}
    for index in length_groups:
        for word in word_groups[index]:
            if users_guess not in word:
                demon_dict.setdefault(index*10, []).append(word)
            elif users_guess in word:
                demon_dict.setdefault(index, []).append(word)
        for x in sorted(demon_dict, key=lambda x: len(demon_dict[x])):
            return demon_dict[x]
        if x/10 == int(x/10):


file_path = "/usr/share/dict/words"
print(demon_list())
