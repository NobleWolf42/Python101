__author__ = 'Landon Stoner'

#This section generates the random number
from random import randrange
randomnumber = int(randrange(1, 101))

#This section makes "Wargames" references.
answer = input("Shall we play a game? \n")
if answer == "y" or answer == "yes" or answer == "YES" or answer == "Yes" or answer == "Y":

#This section sets the guess counter to zero and the guess number to zero
    totalguess = 0
    guessnumber = 0

#This section prompts the user for guesses, compares the guesses them to the random number, and adds to the guess counter
    print("I have a number between 1 and 100. Can you guess it?")
    while guessnumber != randomnumber:
        guessnumber = int(input("What is your guess? \n"))
        totalguess = totalguess + 1
        if guessnumber < randomnumber:
            print("Your number is too low.\n")
        elif guessnumber > randomnumber:
            print("Your guess is too high.\n")
        elif guessnumber <= 0 or guessnumber > 101:
            print("Your number is out of bounds.\n")

#This section informs the user that they guessed the correct number and how many guesses it took them
    print("You guessed the correct number.")
    print("It took you", totalguess, "guesses.")
