from word_guessing_game import WordGuessGame

def main():
    name = input("What is your name? ")

    # List where all of the words are contained
    word_list = ['rainbow', 'computer', 'science', 'programming',
                 'python', 'mathematics', 'player', 'condition',
                 'reverse', 'water', 'board', 'geeks']

    game = WordGuessGame(name, word_list)    # Assigned the variable to call the class 
    game.start_game()

    while game.turns > 0:          # If the player's turn ran out, then it will display the defeat message
        failed = game.display_word() 
        if game.check_win(failed):      
            break

        game.play_turn()

        if game.check_loss():
            break

if __name__ == "__main__":
    main()