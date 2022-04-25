from words import getWords
import random

class Hangman:
    def __init__(self):
        self.word = random.choice(getWords())
        self.display = ["_" for letter in self.word]
        self.guesses = 0
    def show_word(self):
        display = "".join(self.display)
        print(f"Guess the word: {display}")