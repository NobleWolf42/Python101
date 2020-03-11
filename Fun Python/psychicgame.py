import random
age=int(input("How old are you? "))
print("You said you were",age,"years old.")
if age< 12:
    print("You can't play this game.")
if age> 11:
    print("You may play this game.")
    print("Welcome!")
    score=0
    number=0
    print("Score =",score)
    user=input("What is you name? ")
    ben="Ben"
    russ="Russ"
    if user.lower()==ben.lower():
        score=score+50
    if user.lower()==russ.lower():
        score=score-1000
    print("You have three guesses to guess the correct animal.")
    print("Each correct guess is worth 250 points. Each wrong guess is worth -75 points.")
    animal="Parrot"
    guess1=input("Guess the animal: ")
    if guess1.lower()==animal.lower():
        score=score+250
        number=number+1
    else:
        score=score-75
    print("Only two more guesses left!")
    guess2=input("Guess the animal: ")
    if guess2.lower()==animal.lower():
        score=score+250
        number=number+1
    else:
        score=score-75
    print("Only one guess left!")
    guess3=input("Guess the animal: ")
    if guess3.lower()==animal.lower():
        score=score+250
        number=number+1
    else:
        score=score-75
    print("No more guesses left!")
    print("You got",number,"out of three correct!")
    print("Score =",score)
    rnumber=random.randint(1,25)
    number2=0
    print("You have three guesses to guess the correct number.")
    print("Each correct guess is worth 1000000 points. Each wrong guess is worth -50 points.")
    guess11=int(input("Guess a number between 1 and 25: "))
    if guess11==rnumber:
        score=score+1000000
        number2=number2+1
    else:
        score=score-50
    print("Only two more guesses left!")
    guess22=int(input("Guess a number between 1 and 25: "))
    if guess22==rnumber:
        score=score+1000000
        number2=number2+1
    else:
        score=score-50
    print("Only one guess left!")
    guess22=int(input("Guess a number between 1 and 25: "))
    if guess22==rnumber:
        score=score+1000000
        number2=number2+1
    else:
        score=score-50
    print("No more guesses left!")
    print("You got",number2,"out of three correct!")
    print("Your Score is",score)
    print("High Score is 3000800 points.")
    print("Game Over.")
    
