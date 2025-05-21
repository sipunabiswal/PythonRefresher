rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper ="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors ="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

import random
def play_game():
    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
    if user_choice < 0 or user_choice > 2:
        print("Invalid choice. Please try again.")
        return

    choices = [rock, paper, scissors]
    print(choices[user_choice])

    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(choices[computer_choice])

    if user_choice == computer_choice:
        print("It's a draw!")
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
        print("You win!")
    else:
        print("You lose!")

if __name__ == "__main__":
    play_game()
    while True:
        play_again = input("Do you want to play again? Type 'yes' or 'no'.\n").lower()
        if play_again == 'yes':
            play_game()
        elif play_again == 'no':
            print("Thanks for playing!")
            break
        else:
            print("Invalid input. Please type 'yes' or 'no'.")