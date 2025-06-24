# guessing game
import random

# Adding the parent class 
class Game:
    def __init__(self, name):
        self.name = name

    def start_game(self):
        print(f"Good Luck, {self.name}!")

# Adding the child class
class WordGuessGame(Game):
    def __init__(self, name, word_list, turns=12):
        super().__init__(name)
        self.word_list = word_list
        self.word = random.choice(word_list)
        self.guesses = ''
        self.turns = turns

    def display_word(self):
            display = ''
            failed = 0

            for char in self.word:
                if char in self.guesses:
                    display += char + ' '     # Displays the letter when the user guessed correctly
                else:
                    display += '_ '    # Displays the underscore when user's answer is incorrect 
                    failed += 1

            print(display.strip())
            return failed

# Handles the users turns (how many turns left)
    def play_turn(self):
        guess = input("Guess a character: ")
        self.guesses += guess      # Adds count to the guesses the user can have if they answered correctly

        if guess not in self.word:
            self.turns -= 1        # Subtracts count from the guesses if the user guessed wrong
            print("Wrong")
            print(f"You have {self.turns} more guesses.")
        else:
            print("Good guess!")

# Checks if the failed guesses are 0
    def check_win(self, failed):   
        if failed == 0:
            print("You Win!")
            print(f"The word is: {self.word}")
            return True
        return False

# Checks if all of the guesses are out, then you are also out
    def check_loss(self):
        if self.turns <= 0:
            print("You Lose")
            print(f"The word was: {self.word}")
            return True
        return False