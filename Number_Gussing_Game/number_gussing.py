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

