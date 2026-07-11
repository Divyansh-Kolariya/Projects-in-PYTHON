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

answer = input("Waht does GPU stands for? ")
if answer == 'graphics processing unit':
    print("Correct")
else:
    print("Incorrect")
    
answer = input("What does RAM stands for? ")
if answer == 'random access memory':
    print("Correct")
else:
    print("Incorrect")

answer = input("What does PSU stands for? ")
if answer == 'power supply unit':
    print("Correct")
else:
    print("Incorrect")