

import random

exit = False
user_points = 0
computer_points = 0

while exit == False:
    options = ["rock", "paper", "scissors"]
    user_input = input("Choose rock, paper, scissors or exit: ")
    computer_input = random.choice(options)


    if user_input == "exit":
        print(100 * "*")
        print("Game ended!")
        print(f"You won a total score of {user_points} and computer total score is {computer_points}")
        exit = True

    if user_input == "rock".lower():
        if computer_input == "rock":
            print("Your input is rock")
            print("Computer input is rock")
            print("It's a tie!")
        elif computer_input == "paper".lower():
            print("Your input is rock")
            print("Computer input is paper")
            print("Computer wins!")
            computer_points += 1
        elif computer_input == "scissors".lower():
            print("Your input is rock")
            print("Computer input is scissors")
            print("You win")
            user_points += 1

    elif user_input == "paper".lower():
        if computer_input == "rock":
            print("Your input is paper")
            print("Computer input is rock")
            print("You win!")
            user_points += 1
        elif computer_input == "paper".lower():
            print("Your input is paper")
            print("Computer input is paper")
            print("It's a tie!")
            
        elif computer_input == "scissors".lower():
            print("Your input is paper")
            print("Computer input is scissors")
            print("Computer wins!")
            computer_points += 1
    
    elif user_input == "scissors".lower():
        if computer_input == "rock":
            print("Your input is scissors")
            print("Computer input is rock")
            print("Computer wins!")
            computer_points += 1
        elif computer_input == "paper".lower():
            print("Your input is scissors")
            print("Computer input is paper")
            print("You win!")
            user_points += 1
        elif computer_input == "scissors".lower():
            print("Your input is scissors")
            print("Computer input is scissors")
            print("It's a tie!")
            

    elif user_input != "rock".lower() or user_input != "paper".lower() or user_input != "scissors".lower() or user_input != "exit".lower():
        print("Invalid input!")
