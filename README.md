# Hangman
Welcome! I hope you enjoy this fun game of Hangman. It was one of my favourite games growing up which is why I decided to create it and it purely using Python.
[View the game which was deployed via heroku](https://hangman-101.herokuapp.com/)
![Resposnsive](assets/readme_pictures/amiresponsive.PNG)

# Strategy plan
Hangman is a short game that can be played by people of all ages. The goal is to guess a letter, if you guess the correct letter it shows the letter in the correct location of that word. Continue guessing until you have guessed all the correct letters in the word. Once you have guessed all letters in the word you have won!

# Goals
* To provide users with a fun, quick game of Hangman.
* To provide an online Hangman game free to the public.
* To challenge my overall general knowledge.
* To challenge myself by seeing if i can guess in the fewest amount of guesses.
* As a user I would like to be given the option to play again or not.
* As a user I would like to know when the game is finished.
* As user I want to have fun and positive experience.

# Game Features
* Players are prompted to guess a letter.
![Guess-Letter](./assets/readme_pictures/guess_a_letter.PNG)

* Players are tasked with guessing a letter, after correct guess the letter will appear.
![Game-board](./assets/readme_pictures/guesses.PNG)

* Once the user has guessed the correct word they will be told in how many guesses they won.
* Once the user has guessed the correct word they will be asked if they want to play again.
![Winner-Screen](./assets/readme_pictures/winner.PNG)

# Testing 
The game been tested manually on PEP8 and no major problems found. Only whitespace errors coming from giving space to functions by putting a whitespace line space between them
![PEP8-test](./assets/readme_pictures/pep_8_validator.PNG)

# Technologies
* GitHub, used for project control.
* Gitpod, used for making the project.
* Heroku, used for Deployment.

# Bugs
* After deployment the game had a couple errors relating to the imports.
* This was fixed by adding the "requests" library to my requirements.txt file.

# Remaining Bugs
* No Bugs Remained.

# Project Deployment
* Sign up/ login to [heroku](https://id.heroku.com/login).
* Set the buildbacks to Python and NodeJs.
* Link Heroku app to repositry.
* click Deploy.

# Credit 
* Code institute for the deployment terminal.
* Youtube tutorials for help with OOP.
* [W3Schools](https://www.w3schools.com/) used to help me with importing modules.