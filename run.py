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

    def get_letter_index(self, guess):
        """
        checks if the guess entered is equal to a letter in the random word
        """
        letter_locations = []
        for index, char in enumerate(list(self.word)):
            if char == guess:
                letter_locations.append(index)
        return letter_locations
    
    def update_view(self, index, letter):
        """
            update self.display at each index
        """
        for num in index:
            self.display[num] = letter

    def check_guess(self, guess):
        """
            Check if guess is correct
        """
        if guess in self.word:
            index = self.get_letter_index(guess)
            self.update_view(index, guess)
    
    
    def check_winner(self):
        """
            check if user has guessed correct letters to complete word
        """
        display = "".join(self.display)
        word = self.word
        if display == word:
            print("You win!")
            return True
    

def game():
    """
        Starts the game, this will run until word has been guessed
    """
    word = Hangman()
    while True:
        guess = input("Guess a letter: \n ")
        word.check_guess(guess)
        word.show_word()
        word.guesses += 1
        if word.check_winner():
            print(f"You guessed the word in {word.guesses} guesses")
            play_again()
            break
 
def play_again():
    """
        Function to see if user wants to play again
    """
    while True:
        question = input("Do you want to play again? Y/N \n")
        if question.upper() == "N":
            break
        game()


game() 