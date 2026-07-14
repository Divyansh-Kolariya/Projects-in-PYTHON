name = input("Type your name: ")
print("Welcome",name,"to this adventure!")

answer = input("You are on a dirt road, it has come to an end you can go left or right. Which way would you like to go? ").lower()

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim accross? Type walk to walk around and swim to swim accross: ").lower()
    if answer == "swim":
        print("You swim across and were eaten by an alligator.")
    elif answer == "walk":
        print("You run out of water, you lost.")
    else:
        print("Not Valid Option")
elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ").lower()
    if answer == "back":
        print("You go back and loss")
    elif answer == "walk":
        print("You Won!")
    else:
        print("Not Valid Option")
else:
    print("Not Valid Option")