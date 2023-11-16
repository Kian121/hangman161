
import random  # Import the random module.

# Create a list containing the names of your 5 favorite fruits.
favorite_fruits = ["Orange", "Mango", "Pineapple", "Raspberry", "grapefruit"]

# Assign this list to a variable called word_list.
word_list = favorite_fruits

# Create the random.choice method and assign to 'word'.
word = random.choice(word_list)



while True:
    # Ask the user to guess a letter
    guess = input("Guess a letter: ")

    # Check if the guess is a single alphabetical character
    if len(guess) == 1 and guess.isalpha():
        # Break out of the loop if parameters are met
        break
    else:
        # Print error message if the guess is invalid
        print("Invalid letter. Please, enter a single alphabetical character.")

# Check if the guess is in the word
if guess in word:
    
    print(f"Good guess! {guess} is in the word.")
else:
    
    print(f"Sorry, {guess} is not in the word. Try again.")

def check_guess(guess, word):
    """
    Function to check if the guessed letter is in the word.
    """
    # Convert the guess to lower case
    guess = guess.lower()

    # Check if the guess is in the word
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

def ask_for_input(word):
    """
    Function to ask the user for a letter guess and validate the input.
    """
    while True:
        # Asking for a letter guess
        guess = input("Guess a letter: ")

        # Check if the guess is a single alphabetical character
        if len(guess) == 1 and guess.isalpha():
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

    # Call check_guess function
    check_guess(guess, word)

# Example word to guess
word = "example"

# Call ask_for_input function
ask_for_input(word)

