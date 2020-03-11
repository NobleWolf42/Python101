__author__ = 'drroot'

#This section prompts the user to input a number in a set range
number = int(input("Please enter an integer from 1 to 5: "))

#This section evaluates the number to make sure it's in the correct range, and "converts" the integer to text
if 0 < number < 6:
    if number == 1:
        numbertext = "one"
    elif number == 2:
        numbertext = "two"
    elif number == 3:
        numbertext = "three"
    elif number == 4:
        numbertext = "four"
    else: number == 5
    numbertext = "five"
    print("You entered the number,", numbertext)

#This is a section that prints if the number is out of range
else:
    print("Your number is out of range")
