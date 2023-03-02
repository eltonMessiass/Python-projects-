# Import random
# define a function to roll the dice
# create a dictionary that will have the values of the dice


import random


def roll_dice():

    # dice_drawing={
    #     1:(

    #     ),
    #     2:(

    #     )
    # }    

    roll = input("Roll the dice? (yes/no): ")

    while roll.lower() == 'yes'.lower():
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        print("Dice rolled: {} and {}".format(dice1, dice2))
        # print("\n".join(dice_drawing(dice1)))
        # print("\n".join(dice_drawing(dice2)))
        # print("\n".join(dice_drawing(dice3)))

        roll = input("Roll again? (yes/no): ")


roll_dice()