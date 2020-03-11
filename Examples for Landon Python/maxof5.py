#This section prompts the user to input the numbers to be compared
print("Please enter five integer values")
number1 = int(input("Number 1: "))
number2 = int(input("Number 2: "))
number3 = int(input("Number 3: "))
number4 = int(input("Number 4: "))
number5 = int(input("Number 5: "))

#This section compares values to determine the largest number
if number1 >= number2:
    largestnumber = number1
else:
    largestnumber=number2
if largestnumber < number3:
    largestnumber = number3
if largestnumber < number4:
    largestnumber = number4
if largestnumber < number5:
    largestnumber = number5

#This statement prints the largest number
print("The largest number is:", largestnumber)