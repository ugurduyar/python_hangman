import random
import json
from urllib.request import urlopen

hangman_stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


url = "https://www.randomlists.com/data/words.json"
response = urlopen(url)
data_json = json.loads(response.read())
random_word = random.choice(data_json["data"])  
norepeat = list(dict.fromkeys(random_word))  # removes duplicates so i can compare it with the right guesses count
right_guesses = []
wrong_guesses = []
def right_wrong():
    if guess in random_word:
        right_guesses.append(guess) # If users guess is in the word, adds it to the right guesses array
        print("Thats correct!")
    else:
        wrong_guesses.append(guess) # if users guess is not in the word, adds it to the wrong guesses array
        print("That was wrong!")

while True:
    print(hangman_stages[len(wrong_guesses)])
    if len(right_guesses) == len(norepeat): # checks the winning condition
        print("Congratulations!!!")
        break
    if len(wrong_guesses) == 6: # checks the losing condition
        print("You've killed him!")
        print("The word was {}".format(random_word)) # prints the right word if you lose
        break
    guess = input("\nMake a guess! \n")[0] # [0] at the end of the line allows us to accept only the first character given by the user
    if guess in right_guesses or guess in wrong_guesses: # checks if user typed that character before
        print("You've guessed it before!")
    else:
        right_wrong() # if that character never been used before, checks if its right or wrong

    for guess in random_word: # this part allows user to see the current situation of the game
        if guess in right_guesses:
            print(guess + " ",end="")
        else:
            print(" _ ",end="")