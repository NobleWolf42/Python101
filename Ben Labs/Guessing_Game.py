from random import randrange
rn = randrange(1,101)
guessed = False
t = 0
while not guessed:
    n = int(input("Guess a number between 1 and 100:"))
    if n == rn:
        print("Congratulations, You correctly guessed the answer!")
        guessed = True
        t = t+1
    elif n > rn:
        print("Your answer is too high, please try again.")
        t = t+1
    elif n < rn:
        print("Your answer is too low, please try again.")
        t = t+1
print("It took you", t, "trys to guess the correct answer of", rn)