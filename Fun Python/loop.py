import random
rnumber=random.randint(1,50)
score=0
number=0
print("You have three guesses to guess the correct number.")
print("Each correct guess is worth 1000000 points. Each wrong guess is worth -50 points.")
#for i in range(1,5):
done=False
#i=1
#while (i<5):
while (not done):
    #i=i+1
    guess1=int(input("Guess a number between 1 and 25, -1 quits: "))
    if guess1==-1:
        done=True;
    elif guess1==rnumber:
        score=score+1000000
        number=number+1
    else:
        score=score-50
#print("You got",number,"out of four correct.")
print("Score=",score)
print("Game Over!")
