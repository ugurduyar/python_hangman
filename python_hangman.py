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



import random
import json
from urllib.request import urlopen
url = "https://www.randomlists.com/data/words.json"
response = urlopen(url)
data_json = json.loads(response.read())
random_word = random.choice(data_json["data"])
norepeat = list(dict.fromkeys(random_word))
# print(random_word) for debug if needed
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
    print(hangman_stages[len(wrong_guesses)])
    if len(right_guesses) == len(norepeat):
        print("Congratulations!!!")
        break
    if len(wrong_guesses) == 6:
        print("You've killed him!")
        print("The word was {}".format(random_word))
        break
    guess = input("\nMake a guess! \n")
    if guess in right_guesses or guess in wrong_guesses:
        print("You've guessed it before!")
    else:
        right_wrong()

    for guess in random_word:
        if guess in right_guesses:
            print(guess + " ",end="")
        else:
            print(" _ ",end="")