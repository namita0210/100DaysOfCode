import random

try:
    user_age = int(input("Please enter your age: "))
    print(f"User is: {user_age} years old.")
except ValueError:
    print(f"You have entered an invalid age as response. Please enter a numerical response, like {random.randint(1,101)}")

