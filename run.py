from words import getWords
import random

class Hangman:
    def __init__(self):
        self.word = random.choice(getWords())
        self.display = ["_" for letter in self.word]
        self.guesses = 0