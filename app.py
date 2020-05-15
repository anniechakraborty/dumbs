# Magic number game by Annie Chakraborty
# About --
# Chose a magic number from one to ten and ask the user to guess it. If the use guesses right then
# display the number else ask the user to guess again

import random

def magic_number_game():
    numberRange = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    magicNumber = random.choice(numberRange)
    currentTurn = 0
    maxTurns = 5

    while currentTurn <= maxTurns :
        currentTurn += 1
        userPickedNumber = int(input("Guess the magic number : "))
        if userPickedNumber == magicNumber:
            print("Bingo! You got the magic number!")
            break
        else:
            print("Wrong answer.")
            if userPickedNumber < magicNumber :
                print("Hint: the magic number is greater than {}".format(userPickedNumber))            
            else:
                print("Hint: the magic number is lesser than {}".format(userPickedNumber))
            print("Turns left : {}".format(maxTurns - currentTurn))

    if currentTurn > maxTurns:
        print("Your guesses were incorrect.")

    userChoice = input("Do you want to play again? (Y/N)")
    if userChoice == "Y":
        magic_number_game()
    else:
        quit()

magic_number_game()
