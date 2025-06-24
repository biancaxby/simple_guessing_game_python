# guessing game
import random

class WordGuessGame:
    def __init__(self, name, word_list, turns=12):
        super().__init__(name)
        self.word_list = word_list
        self.word = random.choice(word_list)
        self.guesses = 0
        self.turns = turns

