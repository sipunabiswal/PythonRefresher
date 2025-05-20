print("Welcome to the Treasure Hunt!")
print("Your mission is to find the hidden treasure.")
print("You are at a crossroad. Do you want to go left or right?")
choice1 = input("Type 'left' or 'right': ").lower()
if choice1 == "left":
    print("You come to a lake. There is an island in the middle of the lake.")
    print("Type 'wait' to wait for a boat. Type 'swim' to swim across.")
    choice2 = input("Type 'wait' or 'swim': ").lower()
    if choice2 == "wait":
        print("You arrive at the island unharmed.")
        print("There is a house with three doors. One red, one yellow, and one blue.")
        print("Which color do you choose?")
        choice3 = input("Type 'red', 'yellow', or 'blue': ").lower()
        if choice3 == "yellow":
            print("You found the treasure! You win!")
        elif choice3 == "red":
            print("You were burned by fire. Game over.")
        elif choice3 == "blue":
            print("You were eaten by beasts. Game over.")
            