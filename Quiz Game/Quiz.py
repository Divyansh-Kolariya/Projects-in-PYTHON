print("Welcome to Quiz")

playing = input("Do you want to play?Y/N ")

if playing.lower() != "yes" and playing.lower() != "y":
    quit()
    
print("Let's Play")

answer = input("What does CPU stands for? ")
if answer.lower() == 'central processing unit':
    print("Correct")
else:
    print("Incorrect")

answer = input("Waht does GPU stands for? ")
if answer.lower() == 'graphics processing unit':
    print("Correct")
else:
    print("Incorrect")
    
answer = input("What does RAM stands for? ")
if answer.lower() == 'random access memory':
    print("Correct")
else:
    print("Incorrect")

answer = input("What does PSU stands for? ")
if answer.lower() == 'power supply unit':
    print("Correct")
else:
    print("Incorrect")