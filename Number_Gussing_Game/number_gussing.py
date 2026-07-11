import random

top_of_range = input("Enter a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range < 0:
        print("Invald Number")
        quit()
else:
    print("Invald Number")
    quit()


random_number = random.randrange(top_of_range)

while True:
    user_guess = input("Enter a Guess: ")

    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Invald Number")
        continue
    
    if user_guess == random_number:
        print("You got it!")
        break
    else:
        print("Wrong Guess")
    
