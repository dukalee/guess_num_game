#!/usr/bin/python3

"""
숫자 맞추기 IQ 게임
Guess the 4-Digit number

PROGRAM NAME: guess_num_game2.py
VERSION: 1.1
CREATOR: dukalee
DATE: February 17, 2018 (last edited)
======================

It's a game to guess a 4 digit number with the smallest number of tries as possible. 
when you enter a 4-digit number, you can get a hint according to your guess. 
1. How many numbers are correct. 
2. How many numbers are correct and in the right position.

4자릿수의 비밀 숫자를 최소한의 횟수로 맞추는 게임입니다. 
4자리의 숫자를 입력하면 비밀 숫자에 대한 힌트를 얻을 수 있습니다. 
1. 자리 '와' 숫자가 맞았는지, 
2. 숫자가 맞았는지 

--------------------------------------------
Guess the Number!4567
Number of Correct Numbers: 1
Number of Correct Numbers at correct Places: 2
--------------------------------------------

라는 힌트를 얻을 수 있습니다. 


VERSION
---------------------
1.1 : changes made so that a 4-digit number containing duplicate numbers will not be created.

"""

import random 

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

    secret_num = create_secret_num()                                               #choose random number between 1000 and 9999
    print(secret_num)
    print(secret_num[1])
    game = True
    tries = 0 

    while game:

        guess = input("Guess the Number!")

        if guess.isdigit(): 
            if len(guess) == 4: 
                tries += 1

                if guess == secret_num:                                                                 #if guess is correct
                    print("You got it! the number is: {}".format(secret_num))
                    print("tries: {}".format(tries))                                                    #show how many tries the player took to guess the number right
                    game = False
                else:
                    c_num = 0                                                                           #number of correct numbers of a guess
                    c_placeandnum = 0                                                                   #number of correct numbers in right places of a guess
                    i = 0 
                    num = ''

                    while i < len(guess):
                        if guess[i] == secret_num[i]:                                                   #if the indexes of two numbers are same (at the same position)
                            c_placeandnum += 1
                        else: 
                            if guess[i] in secret_num:                                                  #if the number is in the secret number and not in 
                                c_num += 1
                                num += guess[i]
                        i+=1
                    print("Number of Correct Numbers: {}".format(c_num))
                    print("Number of Correct Numbers at correct Places: {}".format(c_placeandnum))
            else:
                print("Enter a 4-digit number!")
        else: 
            print("Enter a Number!")


if __name__ == "__main__":
    game()