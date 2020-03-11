__author__ = 'Stoner'

#This section allows the user to input a variable number of integers.
#The data input will be ended once the user inputs a negative number
in_value = 0
max = -1
while in_value >= 0:
    in_value = int(input("Enter a positive integer (-1 quits the data entry) "))
    if max < in_value:
        max = in_value
if (max > -1):
    print("The maximum value entered is,", max)
else: print("You did not enter a valid number.")
