import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list).lower()
        self.word_guessed = ['_' for _ in self.word]
        self.num_lives = num_lives
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[i] = guess
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word. You have {self.num_lives} lives left.")

    def ask_for_input(self):
        while True:
            guess = input("Guess a letter: ")
            if not (len(guess) == 1 and guess.isalpha()):
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.list_of_guesses.append(guess)
                self.check_guess(guess)
                break

    def has_won(self):
        return all(letter in self.list_of_guesses for letter in self.word)

    def play(self):
        while True:
            if self.num_lives == 0:
                print(f"You lost! The word was '{self.word}'.")
                break
            elif self.has_won():
                print(f"Congratulations. You won the game! The word was '{self.word}'.")
                break
            else:
                print(' '.join(self.word_guessed))
                self.ask_for_input()


# List of words to use in the game
word_list = ["Orange", "Mango", "Pineapple", "Raspberry", "Grapefruit"]

# Initialize and play the game
hangman_game = Hangman(word_list)
hangman_game.play()
