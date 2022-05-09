import random
from words import get_words


class Hangman:
    """
    Class for a hangman game
    """
    def __init__(self):
        """
        holds the innit variables of the word, display and how many guesses
        """
        self.word = random.choice(get_words())
        self.display = ["_" for letter in self.word]
        self.guesses = 0

    def show_word(self):
        """
        Displays the letter placeholder "_" in the terminal
        """
        display = "".join(self.display)
        print(f"Guess the word: {display}")

    def get_letter_index(self,guess):
        """
        checks if the guess entered is equal to a letter in the random word
        """
        letter_locations = []
        for index ,char in enumerate(list(self.word)):
            if char == guess:
                letter_locations.append(index)
        return letter_locations
    
    def update_view(self, index, letter):
        """
            update self.display at each index
        """
        for num in index:
            self.display[num] = letter

