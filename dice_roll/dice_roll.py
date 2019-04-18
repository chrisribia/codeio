from random import randint 

def dice_roll():
    scores = randint(1,6)
    return scores

def user_input():
        roll = input("Please enter y  to continue or anything else to quit : ")
        return roll

def game():
        results = user_input()
        while results.lower() == 'y': 
                print(dice_roll())
                results = user_input()               
        return ("thanks for playing")
#print(game())
