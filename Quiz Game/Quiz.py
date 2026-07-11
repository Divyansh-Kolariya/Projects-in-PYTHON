print("Welcome to Quiz")

playing = input("Do you want to play? ")

if playing != "yes":
    quit()
    
print("Let's Play")

answer = input("What does CPU stands for? ")
if answer == 'central processing unit':
    print("Correct")
else:
    print("Incorrect")