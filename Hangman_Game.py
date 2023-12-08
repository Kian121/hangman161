import random


class Hangman:
    """
    A Hangman game class which represents a single game session.

    Attributes:
        word (str): The word to be guessed.
        word_guessed (list): List representing the characters guessed by the user.
        num_letters (int): The number of unique letters in the word.
        num_lives (int): The number of lives the user has.
        list_letters (list): List of letters that have been guessed.
    """
    
    def __init__(self, word_list, num_lives=5):
        """
        Initializes a new game of Hangman with a randomly selected word from the given list.

        Parameters:
            word_list (list of str): A list of words from which the game randomly chooses one.
            num_lives (int): The number of incorrect guesses allowed before the game is lost (default is 5).
        """
        self.word = random.choice(word_list).lower()  # The mystery word
        self.word_guessed = ['_' for _ in self.word]  # List to track the guessed word
        self.num_letters = len(set(self.word))  # Counts the unique letters in the word
        self.num_lives = num_lives  # Number of lives the player starts with
        self.list_letters = []  # List to keep track of guessed letters

        # Initial message to the player.
        print(f"The mystery word has {self.num_letters} unique characters.")
        print(' '.join(self.word_guessed))

    def check_letter(self, letter):
        """
        Processes the player's letter guess and updates the game's state accordingly.

        If the letter is in the word and hasn't been guessed before, it reveals the letter's position(s) in the word.
        If the letter is not in the word, it decrements the number of lives left.

        Parameters:
            letter (str): The letter guessed by the player.

        Returns:
            None
        """
        letter = letter.lower()
        if letter not in self.list_letters:
            self.list_letters.append(letter)

        if letter in self.word:
            if letter not in self.word_guessed:
                self.num_letters -= 1
            
            for i, char in enumerate(self.word):
                if char == letter:
                    self.word_guessed[i] = letter
        else:
            self.num_lives -= 1
            print(f"Sorry, {letter} is not in the word. You have {self.num_lives} lives left.")

    def ask_letter(self):
        """
        Requests a letter from the player and ensures it is a valid single alphabetical character.
        Re-prompts the player until a valid letter is entered.

        Returns:
            None
        """
        while True:
            letter = input("Guess a letter: ")
            if len(letter) != 1 or not letter.isalpha():
                print("Please, enter just one alphabetical character.")
            elif letter in self.list_letters:
                print(f"You have already tried '{letter}'.")
            else:
                self.check_letter(letter)
                break


def play_game(word_list):
    """
    Begins and manages a game of Hangman.

    Continues to prompt for guesses until the player either wins (guesses all letters) or loses (runs out of lives).

    Parameters:
        word_list (list of str): A list of words from which the game randomly chooses one to start a new game.

    Returns:
        None
    """
    game = Hangman(word_list, num_lives=5)
    while True:
        if game.num_lives == 0:
            print(f"You lost! The word was '{game.word}'.")
            break
        elif '_' not in game.word_guessed:
            print("Congratulations! You won!")
            print(f"The word was '{game.word}'.")
            break
        else:
            print(' '.join(game.word_guessed))
            game.ask_letter()


if __name__ == '__main__':
    # List of words used for the Hangman game
    word_list = ["orange", "mango", "pineapple", "raspberry", "grapefruit"]
    play_game(word_list)
