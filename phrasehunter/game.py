import random
import os

from phrase import Phrase
from character import Character

PHRASES_LIST = ['Hit the sack', 'Lose your touch', 'Sit tight',
              'Pitch in', 'Go cold turkey', 'Ring a bell',
              'Break Even', 'Keep your chin up', 'Rule of Thumb',
              'A piece of cake']

y_valid = {"yes": "yes", "y": "yes"}
n_valid = {"no": "no", "n": "no"}


class Game:
    def __init__(self, phrases):
        self.guessed_letters = set()
        self.phrase = list(random.choice(phrases))
        self.guess_box = ["_" if char.isalpha() else char for char in self.phrase]
        self.secret_letters = {char.lower() for char in self.phrase if char.isalpha()}
        self.players_lives = 5

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def welcome(self):
        print("-"*31)
        print(" "*7, "PH_ASE H_NTER");
        print("-"*31)
        print("Welcome to Phrase Hunter game")
        print("The rule is pretty simple. Just Guess!\n")
        while True:
            play = input("Shall we play? (Yes/No): ").lower()
            if play in y_valid.keys():
                self.main_game()
                break
            elif play in n_valid.keys():
                print("Okay, bye now!")
                break
            else:
                print("That's not a valid option. Please Try again.\n")

    def main_game(self):
        while True: #...
            self.clear_screen()
            
            #self.display_phrase()
            if self.players_lives == 0:
                print("GAME OVER. The answer is '{}'. Better luck next time!".format(''.join(self.phrase).upper()))
                self.replay()
                break
            else:
                print("")
                print(' '.join(self.guess_box))
                player_choice = input("\nguess a letter: ").lower()
                if not (player_choice.isalpha()):
                    print("Oops! That's not a letter. Try again.\n")
                elif len(player_choice) > 1:
                    print("That's more than a letter! Try again.")
                elif player_choice in self.guessed_letters:
                    print("You've used that letter!.")
                elif player_choice in self.secret_letters:# self.secret_letters:
                    print("Nice! You've got it. Keep em coming!")
                    self.guessed_letters.add(player_choice)
                    for index, value in enumerate(self.phrase):
                        if value.lower() == player_choice:
                            self.guess_box[index] = value
                else:
                    print("Sorry, That's a MISS!\n")
                    self.guessed_letters.add(player_choice)
                    self.players_lives -= 1

    def replay(self):
        while True:
                play = input("Would you like to play again? (Yes/No): ").lower()
                if play in y_valid.keys():
                    self.main_game()
                    break
                elif play in n_valid.keys():
                    print("\nThanks for playing, bye now!")
                    break
                else:
                    print("That's not a valid option. Please Try again.\n")


if __name__ == '__main__':
    run = Game(WORDS_LIST)
    run.welcome()
