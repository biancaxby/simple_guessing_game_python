# guessing game
import random

class WordGuessGame:
    def __init__(self, name, word_list, turns=12):
        super().__init__(name)
        self.word_list = word_list
        self.word = random.choice(word_list)
        self.guesses = 0
        self.turns = turns

def display_word(self):
            display = ''
            failed = 0

            for char in self.word:
                if char in self.guesses:
                    display += char + ' '
                else:
                    display += '_ '
                    failed += 1

            print(display.strip())
            return failed

guess_game = WordGuessGame
guess_game.display_word()