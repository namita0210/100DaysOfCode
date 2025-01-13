import random

word_list = ["Apple", "Banana", "Mangoes"]
chosen_word = random.choice(word_list)

placeholder = "_"* len(chosen_word)
print(f"Guess the letters to complete the word in {placeholder}")

correct_word = []

game_over = False

while not game_over:

    guess = input("Enter your guess: ").lower()
    print(f"You guessed: {guess}")

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_word.append(letter)
        else:
            display+="_"   

    print(display)             

    if "_" not in display:
        game_over = True



