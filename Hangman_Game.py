import random

class Hangman:
    """
    A Hangman game class which represents a single game.
    
    Attributes:
        word (str): The word to be guessed.
        word_guessed (list): List representing the characters guessed by the user.
        num_letters (int): The number of unique letters in the word.
        num_lives (int): The number of lives the user has.
        list_letters (list): List of letters that have been guessed.
    """
    
    def __init__(self, word_list, num_lives=5):
        """
        The constructor for Hangman class.
        
        Parameters:
            word_list (list): The list of words from which the game chooses.
            num_lives (int): The number of lives the player starts with (default is 5).
        """
        self.word = random.choice(word_list).lower()  # The mystery word
        self.word_guessed = ['_' for _ in self.word]  # List to track the guessed word
        self.num_letters = len(set(self.word))  # Counts the unique letters in the word
        self.num_lives = num_lives  # Number of lives the player starts with
        self.list_letters = []  # List to keep track of guessed letters

        # Prints the number of unique letters in the word
        print(f"The mystery word has {self.num_letters} characters")
        print(' '.join(self.word_guessed))

    def check_letter(self, letter):
        """
        Check if the letter provided by the user is in the word and update game state accordingly.
        
        Parameters:
            letter (str): The letter to check.
            
        Returns:
            None
        """
        letter = letter.lower()
        if letter in self.word:
            if letter not in self.list_letters:
                self.num_letters -= 1
                self.list_letters.append(letter)
            for i, char in enumerate(self.word):
                if char == letter:
                    self.word_guessed[i] = letter
        else:
            self.num_lives -= 1
            print(f"Sorry, {letter} is not in the word. You have {self.num_lives} lives left.")

    def ask_letter(self):
        """
        Prompt the player to input a letter and validate it.
        
        Returns:
            None
        """
        while True:
            letter = input("Guess a letter: ")
            if len(letter) != 1 or not letter.isalpha():
                print("Please, enter just one character")
            elif letter in self.list_letters:
                print(f"{letter} was already tried")
            else:
                self.check_letter(letter)
                break

def play_game(word_list):
    """
    Function to initiate and control the flow of the Hangman game.
    
    Parameters:
        word_list (list): The list of words from which the game chooses.
        
    Returns:
        None
    """
    game = Hangman(word_list, num_lives=5)
    while True:
        if game.num_lives == 0:
            print(f"You lost! The word was '{game.word}'.")
            break
        elif game.num_letters == 0:
            print("Congratulations! You won!")
            break
        else:
            print(' '.join(game.word_guessed))
            game.ask_letter()

if __name__ == '__main__':
    # List of words used for the Hangman game
    word_list = ["orange", "mango", "pineapple", "raspberry", "grapefruit"]
    play_game(word_list)
