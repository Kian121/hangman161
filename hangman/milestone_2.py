# Ask user to input a single letter.
# Assign the input to the variable 'guess'.
guess = input("Input a letter: ")
# Create an if statement to check if the length of the input is equal to 1 and the input is alphabetical.
if len(guess) == 1 and guess.isalpha():
    # Print "Good guess!" if the conditions are met.
    print("Good guess!")
else:
    # Print "Oops! That is not a valid input." if the conditions are not met.
    print("Oops! That is not a valid input.")



import random  # Import the random module.

# Create a list containing the names of your 5 favorite fruits.
favorite_fruits = ["Orange", "Mango", "Pineapple", "Raspberry", "grapefruit"]

# Assign this list to a variable called word_list.
word_list = favorite_fruits

# Create the random.choice method and assign to 'word'.
word = random.choice(word_list)

# Printthe word.
print(word)

# Print out the newly created list.
print(word_list)
