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

    def play_turn(self):
        guess = input("Guess a character: ")
        self.guesses += guess

        if guess not in self.word:
            self.turns -= 1
            print("Wrong")
            print(f"You have {self.turns} more guesses.")
        else:
            print("Good guess!")

    def check_win(self, failed):
        if failed == 0:
            print("You Win!")
            print(f"The word is: {self.word}")
            return True
        return False

    def check_loss(self):
        if self.turns <= 0:
            print("You Lose")
            print(f"The word was: {self.word}")
            return True
        return False

guess_game = WordGuessGame
guess_game.display_word()
guess_game.play_turn()
guess_game.check_win()
guess_game.check_loss()