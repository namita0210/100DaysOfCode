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

letters = [ 
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = [ '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' ]
symbols = [
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+',
    '[', ']', '{', '}', '|', '\\', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/', '`', '~'
]

password = ""
n_chars = int(input("Enter the number of characters you want in your password : "))
n_symbols = int(input("Enter the number of symbols you want in your password : "))
n_nums = int(input("Enter the number of digits you want in your password : "))

for i in range(0, n_chars):
    ch = random.choice(letters)
    password += ch

for i in range(0, n_symbols):
    ch = random.choice(symbols)
    password += ch

for i in range(0, n_nums):
    ch = random.choice(numbers)    
    password += ch

print(f"The password is : {password}")    
