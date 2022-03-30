from ast import Try
from dictionary import dictionary
import random

class BruteForce:

    def __init__(self) -> None:
        self.word_bank = dictionary.five_letter.copy()
        self.turn = 0
        self.guessed_words = []
        self.guessed_letters = set()
        self.excluded_letters = set()
        self.used_letters = set()
        self.correct_letters = [0,0,0,0,0]

    def guess_word(self, word = None):
        if word:
            guess_word = word
        elif(len(self.guessed_words) == 0):
            guess_word = dictionary.pick_a_word()
        else:
            guess_word = self.predict_word()
        self.guessed_words.append(guess_word)
        self.turn += 1
        # print("Guessing: ",self.guessed_words)
        return guess_word
    
    def predict_word(self):
        # optimize
        # at this point, word_bank should be cleaned...
        word = random.choice(self.word_bank)
        self.word_bank.remove(word) # remove the word from the bank
        return word

    
    def update_state(self, env_state):
        # [R,A,I,S,E]
        # [0,0,0,0,0]
        # [
        # [1, 1, -1, -1, 1],
        # [1, 1, 1, 5, 1], 
        # [5, 5, 5, 5, 5], 
        # [0, 0, 0, 0, 0], 
        # [0, 0, 0, 0, 0], 
        # [0, 0, 0, 0, 0]
        # ]
        # if env_state falsy, not a word
        if not env_state:
            return None
        self.state = env_state
        try:
            guessed_word = self.guessed_words[self.turn-1]
            row = self.state[self.turn-1]
        except Exception as e:
            # print("Error:",e)
            return False
        # print(self.state, self.turn)
        # print(self.turn, "Update State", env_state)
        if row == [5, 5, 5, 5, 5]:
            return True
        for r in range(5):
            if row[r] == 5:
                self.correct_letters[r] = guessed_word[r]
                self.words_with_letter_at(guessed_word[r], r)
            elif row[r] == 1:
                self.used_letters.add(guessed_word[r])
                self.words_with_letter_in(guessed_word[r])
            elif row[r] == -1:
                self.excluded_letters.add(guessed_word[r])
                self.eliminate_words(guessed_word[r])
        
        
        # print(self.correct_letters,self.used_letters,self.excluded_letters, len(self.word_bank))
        return None
    
    def eliminate_words(self, letter):
        new_bank = []
        for w in self.word_bank:
            if letter not in w:
                new_bank.append(w)
        self.word_bank = new_bank
    
    def words_with_letter_at(self, letter, pos):
        new_bank = []
        for w in self.word_bank:
            if w[pos] == letter:
                new_bank.append(w)
        self.word_bank = new_bank
    
    def words_with_letter_in(self, letter):
        new_bank = []
        for w in self.word_bank:
            if letter in w:
                new_bank.append(w)
        self.word_bank = new_bank