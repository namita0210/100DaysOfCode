import random

# List of words to guess
word_list = ["camel", "baboon", "america"]
# Randomly select a word from the word list
chosen_word = random.choice(word_list)
print(f"Chosen Word: {chosen_word}")

# Create a placeholder string for visual representation with blanks
placeholder = "_ " * len(chosen_word)
print(f"Word to guess: {placeholder.strip()}")  # Trim the trailing space

game_over = False
correct_letters = []

while not game_over:
    # Ask the user for a guess
    guess = input("Enter a guess letter that you think would be there in the chosen word: ").lower()
    
    # If the letter has already been guessed
    if guess in correct_letters:
        print("You've already guessed that letter!")
    else:
        # Add the guess to the correct letters list if it's part of the word
        if guess in chosen_word:
            print(f"Correct! '{guess}' is in the word.")
            correct_letters.append(guess)
        else:
            print(f"Sorry! '{guess}' is not in the word.")
    
    # Update the display based on correct guesses
    display = ""
    for letter in chosen_word:
        if letter in correct_letters:
            display += letter + " "
        else:
            display += "_ "

    # Trim trailing spaces and show progress
    print("Current word state: ", display.strip())

    # Check if the game has been won
    if "_" not in display:
        game_over = True
        print("Congratulations! You've guessed the word correctly.")
    else:
        print("Keep guessing...")
