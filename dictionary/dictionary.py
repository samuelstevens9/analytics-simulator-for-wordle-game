
import re
import random

all_words = []
five_letter = []

with open("dictionary/usa2.txt", "r") as words_file:
    all_words = words_file.read().splitlines()
    for word in all_words:
        if len(word) == 5 and not re.findall('[A-Z]', word):
            five_letter.append(word)

def pick_a_word():
    return random.choice(five_letter)

def is_a_word(word):
    return word in five_letter

