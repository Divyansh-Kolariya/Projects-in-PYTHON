import random

user_wins = 0
computer_wins = 0
options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to Quit: ").lower()
    if user_input == 'q':
        break
        
    if user_input not in options:
        continue
    
    random_num = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    
    computer_pick = options[random_num]
    print("Computer picked", computer_pick + ".")
    
    if user_input == computer_pick:
        print("Draw")
    elif user_input[0] and computer_pick[2]:
        user_wins += 1
        print("You Won")
    elif user_input[2] and computer_pick[1]:
        user_wins += 1
        print("You Won")
    else:
        print("You Lost")
        computer_wins += 1
        
print("You won",user_wins,"times")
print("Computer won",computer_wins,"times")
print("Goodbye!")