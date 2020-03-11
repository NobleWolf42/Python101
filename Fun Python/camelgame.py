import random

print("Welcome to Camel!")
print("")
print("You have stolen a camel to make your way across the Great Mobi desert.")
print("The natives want their camel back and are chasing you down!")
print("Survive your desert trek and outrun the natives.")
print("")
print("If you find an oasis the natives stop and your camel rests while")
print("you drink and fill your canteen!")
print("")
done=False
rreplay=True
miles=0
water=0
camel=0
native=-20
canteen=5
while (rreplay==True):
    while(not done):
        rnat1=random.randint(7,14)
        rmil1=random.randint(10,20)
        rmil2=random.randint(5,12)
        cmltir1=random.randint(1,3)
        cmltir2=random.randint(0,1)
        native2=miles-native
        r=random.randint(1,20)
        print("")
        print("A. Drink from your canteen.")
        print("B. Ahead moderate speed.")
        print("C. Ahead full speed.")
        print("D. Stop for the night.")
        print("E. Status check.")
        print("Q. Quit.")
        user_choice=input("Your Choice? ")
        print("")
        if user_choice.lower()=="q":
            print("Game Over")
            done=True;
        elif user_choice.lower()=="e":
            print("Miles Traveled:",miles)
            print("Drinks left in your canteen:",canteen)
            print("The natives are",native2,"miles behind you.")
        elif user_choice.lower()=="d":
            camel=0
            native=native+rnat1
            print("Your camel is happy!")
        elif user_choice.lower()=="c":
            miles=miles+rmil1
            water=water+1
            camel=camel+cmltir1
            native=native+rnat1
            print("You traveled",rmil1,"miles.")
        elif user_choice.lower()=="b":
            miles=miles+rmil2
            water=water+1
            camel=camel+cmltir2
            native=native+rnat1
            print("You traveled",rmil2,"miles.")
        elif user_choice.lower()=="a":
            if canteen>0:
                water=0
                canteen=canteen-1
                print("You have",canteen,"drinks left.")
            else:
                print("You don't have any water left in your canteen!")
        else:
            print("That choice is invalid.")
        if water>6:
            print("Game Over")
            print("You died of thirst.")
            done=True
            rreplay=False
        elif water>3:
            print("You are thirsty.")
        if camel>8:
            print("Game Over")
            print("Your camel died.")
            done=True
            rreplay=False
        elif camel>5:
            print("Your camel is tired.")
        if native2<=0:
            print("Game Over")
            print("The natives caught you.")
            done=True
            rreplay=False
        elif native2<15:
            print("The natives are getting close.")
        if r==5:
            canteen=canteen+5
            water=0
            camel=0
            print("You found an oasis!")
        if miles>=200:
            print("Congradulations, You Won The Game!!!")
            done=True
            rreplay=False
    replay=input("Do you want to play again? (y/n) ")
    if replay.lower()=="y":
        rreplay=True
        done=False
        miles=0
        water=0
        camel=0
        native=-20
        canteen=5
    elif replay.lower()=="n":
        print("Quitting...")
    else:
        print("Invalid Response")
