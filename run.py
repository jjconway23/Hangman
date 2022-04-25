from words import getWords
import random

class Hangman:
    """
    Class for a hangman game
    """
    def __init__(self):
        """
        holds the innit variables of the word, display and how many guesses
        """
        self.word = random.choice(getWords())
        self.display = ["_" for letter in self.word]
        self.guesses = 0
    def show_word(self):
        """
        Displays the letter placeholder "_" in the terminal
        """
        display = "".join(self.display)
        print(f"Guess the word: {display}")