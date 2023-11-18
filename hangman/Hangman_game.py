import random

class Hangman:
    def __init__(self, word_list, num_lives=5):# Chooses a random word from the list and initialises the game variables
        self.word = random.choice(word_list).lower() # The mystery word
        self.word_guessed = ['_' for _ in self.word] # List to track the guessed word
        self.num_letters = len(set(self.word))  # Counts the unique letters in the word
        self.num_lives = num_lives # Number of lives the player starts with
        self.list_letters = [] # List to keep track of guessed letters

        # Prints the number of unique letters in the word
        print(f"The mystery word has {self.num_letters} characters")
        print(' '.join(self.word_guessed))

    def check_letter(self, letter) -> None: # Converts the guessed letter to lowercase and checks if it is in the mystery word
        letter = letter.lower()
        if letter in self.word: # Updates the word_guessed list and reduces num_letters for a correct guess
            if letter not in self.list_letters:
                self.num_letters -= 1
                self.list_letters.append(letter)
            for i, char in enumerate(self.word):
                if char == letter:
                    self.word_guessed[i] = letter
        else:
            self.num_lives -= 1 # Reduces the number of lives by 1 if the guessed letter is not in the word 
            print(f"Sorry, {letter} is not in the word. You have {self.num_lives} lives left.")

    def ask_letter(self):   # Loop to keep asking player to guess a valid letter
        while True:
            letter = input("Guess a letter: ")
            if len(letter) != 1 or not letter.isalpha():
                print("Please, enter just one character")
            elif letter in self.list_letters:
                print(f"{letter} was already tried")
            else:
                self.check_letter(letter)
                break

def play_game(word_list): # Begins the game with the list of chosen words
    game = Hangman(word_list, num_lives=5)
    while True: # Game loop that continues until the player wins or loses
        if game.num_lives == 0: # Prints message if player runs out of lives 
            print(f"You lost! The word was '{game.word}'.")
            break
        elif game.num_letters == 0: # Finishes the game if the player guesses correctly
            print("Congratulations! You won!")
            break
        else: # Shows the correct guesses of the word and asks player to input the next letter
            print(' '.join(game.word_guessed))
            game.ask_letter()
            
if __name__ == '__main__':
    # List of words used for the Hangman game
    word_list = ["orange", "mango", "pineapple", "raspberry", "grapefruit"]
    play_game(word_list)