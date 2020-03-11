number = int(input("Please enter an integer from 1 to 5--> "))
if 0 < number < 6:
    if number == 1:
        print("You entered one")
    elif number == 2:
        print("You entered two")
    elif number == 3:
        print("You entered three")
    elif number == 4:
        print("You entered four")
    else:
        print("You entered five")
else:
    print("Your number is out of range")
    
print("Done")