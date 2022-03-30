import re
from dictionary import dictionary


class Game:

    def __init__(self,wordle_word = None) -> None:
        self.total_tries = 6
        self.tries = 0
        self.try_matrix = [
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0]
        ]
        if not wordle_word:
            self.wordle_word = dictionary.pick_a_word()
        else:
            self.wordle_word = wordle_word

    def new_game(self):
        self.tries = 0
        self.try_matrix = [
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0]
        ]
        self.wordle_word = dictionary.pick_a_word()
    
    def try_word(self, word):
        # print(self.tries, "Trying:", word, '(',self.wordle_word,')',word == self.wordle_word)
        if self.tries == 6:
            return self.try_matrix
        if not dictionary.is_a_word(word):
            return None
        if word == self.wordle_word:
            self.try_matrix[self.tries] = [5,5,5,5,5]
        else:
            self.try_matrix[self.tries] = self.check_word(word)
        self.tries += 1
        return self.try_matrix
    
    def check_word(self, word):
        row = [0,0,0,0,0]
        for x in range(5):
            if self.is_letter_correct(word[x],x):
                row[x] = 5
            elif self.is_letter_in_word(word[x]):
                row[x] = 1
            else:
                row[x] = -1
        return row
        
    def is_letter_correct(self, letter, pos):
        return letter == self.wordle_word[pos]

    def is_letter_in_word(self, letter):
        return re.findall(letter, self.wordle_word)

        

        