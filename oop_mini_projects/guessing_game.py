import random

flag = False

def game(user_guess, comp_num):         
    if user_guess == comp_num:
        global flag
        flag = True
        print("Congrats! You guessed the right number!") 
    elif user_guess < comp_num:
        print(f"Try again, your guessed number is too low.")
    else:
        print(f"Try again, your guessed number is too high.")          

num1 = random.randint(10,50)
num2 = random.randint(num1,100)

comp_num = random.randint(num1,num2)

user = input("Hello what is your name? ")
print(f"Well, {user} I am thinking of a number between {num1} and {num2}.\nTake a guess...")

try:
    user_guess = int(input(" "))        
except:
    print("Please enter a valid number.")  
    user_guess = int(input("Take a guess again ... "))      

for _ in range(5):
    if(flag == False):
        game(user_guess, comp_num)
        


