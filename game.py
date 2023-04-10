import random

# Define a list of possible secret words
words = ['apple', 'banana', 'cherry', 'orange', 'pear']

# Select a random word from the list
secret_word = random.choice(words)

# Create a list to keep track of guessed letters
guessed_letters = []

# Define a function to display the current state of the secret word
def display_word():
    for letter in secret_word:
        if letter in guessed_letters:
            print(letter, end=' ')
        else:
            print('_', end=' ')
    print()

# Start the game
print('Welcome to the secret word game!')

while True:
    # Display the current state of the secret word
    display_word()
    
    # Ask the user to guess a letter
    guess = input('Guess a letter: ').lower()
    
    # Check if the letter has already been guessed
    if guess in guessed_letters:
        print('You already guessed that letter.')
        continue
    
    # Add the letter to the list of guessed letters
    guessed_letters.append(guess)
    
    # Check if the letter is in the secret word
    if guess in secret_word:
        print('Correct!')
    else:
        print('Incorrect.')
    
    # Check if the user has guessed all the letters in the secret word
    if all(letter in guessed_letters for letter in secret_word):
        print('Congratulations, you guessed the secret word!')
        break
