# # print(True)
# # print(False)
# # print(123)
# # print( 12 + 1)
# # print(123_456_789)

# #print("The number of letters in your name  : " + len(int(input("Your Name: "))))

# # print(False or True or False)

# a = 5
# b = 7
# if a >= b and a != b:
#     print("A")
# elif not a >= b and a != b:
#     print("B")
# else:
#     print("C")        

import random

# heads_or_tails = random.randint(0,1)
# print(heads_or_tails)

# if heads_or_tails == 1:
#     print("Heads")
# else:
#     print("Tails")    

# friends = ["Alice", "Bob", "Charlie", "Emanuel", "Chris"]

# name_idx = random.randint(0, len(friends)-1)

# print(friends[name_idx])

# choices = ["Rock", "Paper", "Scissor"]
# computer = random.randint(0,2)
# computer_choice = choices[computer]

# user_choice = int(input("Enter 0 for Rock, 1 for Paper, and 2 for Scissor"))

# if user_choice == computer_choice:
#     print("Draw")
# elif     
# sum = 0
# for num in range ( 1, 101):
#     sum = sum +num
# print(sum) 
# 

# letters = [ 
#     'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
#     'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
#     'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
#     'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
# ]
# numbers = [ '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' ]
# symbols = [
#     '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+',
#     '[', ']', '{', '}', '|', '\\', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/', '`', '~'
# ]

# password = ""
# n_chars = int(input("Enter the number of characters you want in your password : "))
# n_symbols = int(input("Enter the number of symbols you want in your password : "))
# n_nums = int(input("Enter the number of digits you want in your password : "))

# for i in range(0, n_chars):
#     ch = random.choice(letters)
#     password += ch

# for i in range(0, n_symbols):
#     ch = random.choice(symbols)
#     password += ch

# for i in range(0, n_nums):
#     ch = random.choice(numbers)    
#     password += ch

# print(f"The password is : {password}")    
# def is_letter_in_chosen_word(chosen_word, letter):
    
#     for i,letter in enumerate(chosen_word):
#         if chosen_word[i] == letter:
#             return i
#     return -1

# len_chosen_word = len(chosen_word)

# for i in range(len_chosen_word):
#     user_guess = input("Guess a letter: ")
#     user_guess.lower()
#     if is_letter_in_chosen_word(chosen_word, user_guess) != -1:
#         print("Right")
#     else:
#         print("Wrong")    

word_list = ["camel", "baboon", "america"]
chosen_word = random.choice(word_list)
print(f" Chosen Word: {chosen_word}")

placeholder = ""
placeholder = "_"* len(chosen_word)

game_over = False
correct_letters = []
while not game_over:
    
    guess = input("Enter a guess letter that you think would be there in the chosen word: ").lower()
    print(f"Guess: {guess}")
    display = ""
    
    for letter in chosen_word:
        if letter == guess:
            display += letter  
            correct_letters.append(guess)
        elif letter in correct_letters:
            display+= letter          
        else:
            display += "_"
    print(display) 

    if "_" not in display:
        game_over=True  



    

