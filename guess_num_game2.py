#!/usr/bin/python3

import random 

def instructions(): 

    """
    function to show instructions to the user. 
    """

    print("""

             ----GUESS THE NUMBER!---

You will be given a secret 4-digit number to guess. 
Every time you enter a 4 digit number, if it is wrong, 
you will be given hints to help you deduce the secret 
number. Your job is to guess it with the smallest attempts
as possible. 

                    GOOD LUCK!
        """)


def create_secret_num(): 

    """
    function to create a secret number, with no duplicates within the numbers
    """

    num = str(random.randint(1000,9999))
    while len(set(num)) < 4: 
        num = str(random.randint(1000,9999))
    return num

def game():

    """
    function to play the game 
    """

    instructions()

    secret_num = create_secret_num()                                              #choose random number between 1000 and 9999
    game = True
    tries = 0 

    while game:

        print("Guess the Number!")
        guess = input(">>> ")

        if guess.isdigit(): 
            if len(guess) == 4: 
                tries += 1

                if guess == secret_num:                                            #if guess is correct
                    print("You got it! the number is: {}".format(secret_num))
                    print("tries: {}".format(tries))                               #show how many tries the player took to guess the number right
                    game = False
                    retry()
                else:
                    c_num = 0                                                      #number of correct numbers of a guess
                    c_placeandnum = 0                                              #number of correct numbers in right places of a guess
                    i = 0 
                    num = ''

                    while i < len(guess):
                        if guess[i] == secret_num[i]:                              #if the indexes of two numbers are same (at the same position)
                            c_placeandnum += 1
                        elif guess[i] in secret_num:                               #if the number of the guess is in the secret number but not at the same position
                            if guess[i] not in num:                                #if that number is not already recorded
                                num += guess[i]                                              
                                c_num += 1
                        i+=1
                    print("Number of Correct Numbers: {}".format(c_num))
                    print("Number of Correct Numbers at correct Places: {}".format(c_placeandnum))
            else:
                print("Enter a 4-digit number!")
        else: 
            print("Enter a Number!")


def retry(): 

    """
    function to ask user if he/she wants to play again
    """

    print("""
        Do you wish to play again? (Y/N)
        """)
    ans = input(">>> ")
    if ans.lower() == 'y': 
        game == True
        game()  
    elif ans.lower() =='n': 
        print("""
            Thank you for playing!
            """)
    else: 
        print("""
            Please enter a valid input (Y/N)
            """)




if __name__ == "__main__":
    game()