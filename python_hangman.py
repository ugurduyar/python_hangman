import random
import json
from urllib.request import urlopen
url = "https://www.randomlists.com/data/words.json"
response = urlopen(url)
data_json = json.loads(response.read())
words = (data_json["data"])
random_word = random.choice(words)
print(random_word)
right_guesses = []
wrong_guesses = []

def right_wrong():
    if guess in random_word:
        right_guesses.append(guess)
        print("Thats correct!")
    else:
        wrong_guesses.append(guess)
        print("That was wrong!")


while True:
    if len(wrong_guesses) == 6:
        break
    guess = input("\nMake a guess! \n")
    if guess in right_guesses or guess in wrong_guesses:
        print("You've guessed it before!")
    else:
        right_wrong()

    for guess in random_word:
        if guess in right_guesses:
            print(guess,end="")
        else:
            print(" _ ",end="")








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
