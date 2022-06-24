import random
import json
from urllib.request import urlopen
url = "https://www.randomlists.com/data/words.json"
response = urlopen(url)
data_json = json.loads(response.read())
words = (data_json["data"])
random_word = (random.choice(words))
i = 0
guess_count = 0
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
words_array = list(random_word)
print(words_array)
print(random_word)
while i < len(random_word):
    print("_ " * len(words_array))
    guess = input("Make a guess! ")
    print(hangman_stages[guess_count])
    if guess_count == 6:
        print("You lost")
        break
    print(guess_count)
    if guess in random_word:
        print("found!")
    else:
        print("Not found")
        guess_count += 1

