import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        """
        Initialize the Hangman class with given word list and number of lives.
        """
        self.word = random.choice(word_list).lower()  # Randomly select a word and convert to lowercase
        self.word_guessed = ['_' for _ in self.word]  # Create a list of '_' for each letter in the word
        self.num_letters = len(set(self.word))  # Number of unique letters in the word
        self.num_lives = num_lives  # Number of lives the player has
        self.word_list = word_list  # The list of possible words
        self.list_of_guesses = []  # List to keep track of guesses

    def check_guess(self, guess):
        """
        Check if the guessed letter is in the word and update word_guessed accordingly.
        """
        guess = guess.lower()  # Convert the guess to lowercase

        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[i] = guess
            if guess not in self.list_of_guesses:
                self.num_letters -= 1
        else:
            # Step 2: If the guess is not in the word
            self.num_lives -= 1  # Reduce num_lives by 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        """
        Ask the user for a letter guess and validate the input.
        """
        while True:
            guess = input("Guess a letter: ")

            if not (len(guess) == 1 and guess.isalpha()):
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break

# Example usage
word_list = ["apple", "banana", "cherry"]
hangman_game = Hangman(word_list)

# Testing the check_guess method
# Note: This function call will not work in this environment due to input restrictions
# hangman_game.ask_for_input()



